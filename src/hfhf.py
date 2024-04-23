import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import os
from PIL import Image
import numpy as np

# Load your dataset and preprocess it
def load_data(dataset_path):
    data = []
    labels = []

    for folder in os.listdir(dataset_path):
        folder_path = os.path.join(dataset_path, folder)

        if os.path.isdir(folder_path):  # Skip non-directory entries
            for filename in os.listdir(folder_path):
                img_path = os.path.join(folder_path, filename)

                # Check if the file is an image
                if not os.path.isfile(img_path) or not img_path.lower().endswith(('.png', '.jpg', '.jpeg')):
                    continue

                image = Image.open(img_path).convert('RGB')
                image = image.resize((224, 224))  # Adjust the size as needed
                data.append(np.array(image))
                labels.append(folder)

    le = LabelEncoder()
    labels = le.fit_transform(labels)
    return np.array(data), np.array(labels)

# Define the CNN model
def create_model(input_shape):
    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(128, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Flatten())
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))  # Binary classification

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    return model

# Load and preprocess data
dataset_path = "/Users/krishgandhi/Desktop/morphism/Dataset"
data, labels = load_data(dataset_path)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

# Create and compile the model
input_shape = X_train[0].shape
model = create_model(input_shape)

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

model.save("/src/morph_detection.keras")

# Evaluate the model
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f'Test accuracy: {test_acc}')

# Make predictions
predictions = model.predict(X_test)