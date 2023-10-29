import cv2
import os
import time

# Ensure a directory exists to store the cropped face images
if not os.path.exists('detected_faces'):
    os.makedirs('detected_faces')

# Load the pre-trained Haarcascades classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open the video
cap = cv2.VideoCapture('http://192.168.0.106:5000/video_feed')

# Face counter
face_count = 0
start_time = time.time()
while True:
    # Read each frame from the video
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame to grayscale (necessary for the Haarcascade classifier)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Loop over the detected faces
    for (x, y, w, h) in faces:
        # Increment the face count
        face_count += 1

        # Crop the face from the frame
        cropped_face = frame[y:y+h, x:x+w]

        # Save the cropped face
        filename = f"detected_faces/face_{face_count}.jpg"
        cv2.imwrite(filename, cropped_face)
end_time = time.time()
# Release the video capture object
cap.release()

cv2.destroyAllWindows()


print("total time = ",(end_time - start_time))