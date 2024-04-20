The AMSL Face Morph Image Data Set is a collection of genuine and morphed face images that can be used to evaluate the detection performance of morphing detection algorithms.

The AMSL Face Morph Image Data Set was created based on images from the Face Research Lab London Set [1] distributed under the CC BY 4.0 license and includes genuine neutral and smiling face images as well as morphed face images. The morphed face images were generated from pairs of genuine face images using the morphing approach described in [2] and referred to as "combined morph". All morphs are half-way morphs meaning that the proportions of both faces in the morphed face are the same. While generating morphed faces only suitable pairs regarding the gender and ethnicity were considered. It means that:
- male faces were morphed with male faces only
- female faces were morphed with female faces only
- white people were morphed with white people only
- east asian people were morphed with east asian people only
etc.

All images were modified in the way to comply with the requirements of the ICAO portrait quality standard for eMRTD [3] and to fit on a chip of an eMRTD. This includes the following steps:
- Cropping according to the ICAO portrait quality standard resulting in the image resolution that is proportional to the passport scale of 531x413 pixels
- Down-scaling to 531x413 pixels
- JPEG compression with a variable quantization factor so that the files have maximal size, but not exceeding 15360 bytes (15kb).

The images are located in three folders:

1. 'londondb_genuine_neutral_passport-scale_15kb' with 102 genuine neutral face images 

2. 'londondb_genuine_smiling_passport-scale_15kb' with 102 genuine smiling face images

3. 'londondb_morph_combined_alpha0.5_passport-scale_15kb' with 2175 morphed face images

The high biometric quality of morphed face images is confirmed by high similarity scores resulting from matching morphed and genuine face images of the same person by a widely established commercial face recognition system. In other words, each of 2175 morphs would fool the face recognition system, if the reference face image is taken from the aforementioned set of 102 neutral or 102 smiling genuine face images.


[1] https://figshare.com/articles/Face_Research_Lab_London_Set/5047666

[2] T. Neubert, A. Makrushin, M. Hildebrandt, C. Kraetzer and J. Dittmann, Extended StirTrace Benchmarking of Biometric and Forensic Qualities of Morphed Face Images, IET Biometrics, Volume 7, Issue 4, pp. 325–332, 2018

[3] A. Wolf, ICAO: Portrait Quality (Reference Facial Images for MRTD), Version 0.7. Standard. International Civil Aviation Organization, 2016
