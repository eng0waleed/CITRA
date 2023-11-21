import tensorflow as tf
import numpy as np

# Check GPU Availability and Set Memory Growth
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        print(f"{len(gpus)} GPU(s) available.")
    except RuntimeError as e:
        print(e)
else:
    print("No GPUs available.")

# Create a simple model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(512, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
])

# Compile the model
model.compile(optimizer='adam',
              loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Generate random data
data = np.random.random((1000, 784))
labels = np.random.randint(10, size=(1000,))

# Train the model and print device info
with tf.device('/GPU:0'):
    history = model.fit(data, labels, epochs=10)
    print("Device that performed the computation: ", tf.test.gpu_device_name())
