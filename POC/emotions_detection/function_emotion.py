import cv2
import numpy as np
import os
import tensorflow as tf
from keras.models import load_model

# Dictionary containing the emotion labels
emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Sad", 5: "Surprised", 6: "Neutral"}

# Function to get the labels
def get_labels(dataset_name):
    if dataset_name == 'fer2013':
        return emotion_dict
    raise ValueError("Dataset not recognized. Please provide a valid dataset name.")

# Load the pre-trained model and its labels
emotion_model_path = 'best_model.h5'
emotion_labels = get_labels('fer2013')

# Load the model
emotion_classifier = load_model(emotion_model_path, compile=False)
emotion_target_size = emotion_classifier.input_shape[1:3]

# Function to preprocess the face image
def preprocess_face(face_image):
    face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
    face_image = cv2.resize(face_image, emotion_target_size)
    face_image = face_image.astype('float32') / 255.0
    face_image = np.expand_dims(face_image, 0)
    face_image = np.expand_dims(face_image, -1)
    return face_image

# Function to detect emotion from an image file
def detect_emotion(image_path):
    if not os.path.isfile(image_path):
        return "Image file not found."

    # Load the image
    face_image = cv2.imread(image_path)

    # Preprocess the face image
    face_image = preprocess_face(face_image)

    # Predict the emotion
    emotion_prediction = emotion_classifier.predict(face_image)
    emotion_label_arg = np.argmax(emotion_prediction)
    emotion_text = emotion_labels[emotion_label_arg]

    return emotion_text

# Example usage
image_path = 'path_to_your_image.jpg'
detected_emotion = detect_emotion(image_path)
print(f"Detected Emotion: {detected_emotion}")
