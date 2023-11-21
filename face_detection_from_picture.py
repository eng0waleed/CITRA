import cv2
import face_recognition
import os

# Ensure a directory exists to store the cropped face images
if not os.path.exists('detected_faces'):
    os.makedirs('detected_faces')

# Using cv2 to read the image
face_image = cv2.imread("./detected_faces/face_2068.jpg")

# Convert the image from BGR to RGB format
face_image_rgb = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)

# Detect face locations directly
face_locations = face_recognition.face_locations(face_image_rgb)

for index, (top, right, bottom, left) in enumerate(face_locations):

    # Crop the face from the frame
    cropped_face = face_image[top:bottom, left:right]

    # Save the cropped face with a unique filename for each face
    filename = f"cropped_face_{index}.jpg"
    cv2.imwrite(filename, cropped_face)
