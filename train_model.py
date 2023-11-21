import pandas as pd
import numpy as np
import os
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import ModelCheckpoint

# Check GPU Availability and Set Memory Growth
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    try:
        # Set GPU memory growth to True
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        print(f"{len(gpus)} GPU(s) available.")
    except RuntimeError as e:
        print(e)
else:
    print("No GPUs available.")

# Load dataset
data = pd.read_csv('fer2013.csv')

# Preprocess function


def preprocess_data(data):
    image_array = np.array([np.fromstring(image, np.uint8, sep=' ')
                           for image in data['pixels']])
    images = image_array.reshape(image_array.shape[0], 48, 48, 1)
    images = images.astype('float32') / 255.0

    labels = to_categorical(data['emotion'])
    return images, labels


images, labels = preprocess_data(data)

# Split dataset
X_train, X_val, y_train, y_val = train_test_split(
    images, labels, test_size=0.2, random_state=42)

# Define the model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(48, 48, 1)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(7, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy',
              metrics=['accuracy'])

# Checkpoint to save the best model
checkpoint = ModelCheckpoint(
    'best_model.h5', monitor='val_loss', mode='min', save_best_only=True, verbose=1)

# Train the model using the GPU
history = model.fit(X_train, y_train, validation_data=(
    X_val, y_val), epochs=50, batch_size=64, callbacks=[checkpoint])

# Load best model
best_model = tf.keras.models.load_model('best_model.h5')

# Evaluate the best model on the validation set
val_loss, val_accuracy = best_model.evaluate(X_val, y_val)
print("Validation Loss:", val_loss)
print("Validation Accuracy:", val_accuracy)
