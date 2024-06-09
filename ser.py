from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
model = load_model("morph_detection_model.h5")  # Load your trained model

def preprocess_image(image_path):
    image = Image.open(image_path).convert('RGB')
    image = image.resize((224, 224))  # Adjust size as needed
    image_array = np.array(image) / 255.0  # Normalize pixel values
    return np.expand_dims(image_array, axis=0)

@app.route('/classify', methods=['POST'])
def classify():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if file:
        # Save the uploaded file
        file_path = "uploads/uploaded_image.jpg"
        file.save(file_path)

        # Preprocess the image
        processed_image = preprocess_image(file_path)

        # Make predictions using the loaded model
        prediction = model.predict(processed_image)

        # Get the class label
        class_label = "Morphed" if prediction[0][0] > 0.5 else "Real"

        return jsonify({"prediction": class_label}), 200

if __name__ == '__main__':
    # Ensure the uploads directory exists
    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    app.run(debug=True)