from function_emotion import detect_emotion

def main():
    # Path to the image you want to analyze
    image_path = 'happy1.jpg'

    # Call the emotion detection function
    detected_emotion = detect_emotion(image_path)

    # Print the result
    print(f"Detected Emotion: {detected_emotion}")

if __name__ == "__main__":
    main()
