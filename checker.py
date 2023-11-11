import tensorflow as tf
import platform
import subprocess
import os

print("Python Version:", platform.python_version())
print("TensorFlow Version:", tf.__version__)

# Check for GPUs in the system
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print(f"\n{len(gpus)} GPU(s) available.")
    for i, gpu in enumerate(gpus):
        print(f"GPU {i}: {gpu.name}")
else:
    print("\nNo GPUs available.")

# Check if CUDA is available
try:
    cuda_version = subprocess.run(
        ["nvcc", "--version"], capture_output=True, text=True, check=True)
    print("\nCUDA Toolkit is installed.")
    print(cuda_version.stdout.split("\n")[-2])
except subprocess.CalledProcessError:
    print("\nCUDA Toolkit is not installed or not in the system's PATH.")

# Check if the NVIDIA driver is installed
try:
    nvidia_smi = subprocess.run(
        ["nvidia-smi"], capture_output=True, text=True, check=True)
    print("\nNVIDIA driver is installed.")
    print(nvidia_smi.stdout)
except subprocess.CalledProcessError:
    print("\nNVIDIA driver is not installed or not in the system's PATH.")

# Check if the correct version of TensorFlow is installed
if tf.__version__[0] == "2":
    print("\nYou have TensorFlow 2.x installed, which should include GPU support by default.")
else:
    print("\nYou have TensorFlow 1.x installed. Consider upgrading to TensorFlow 2.x for improved GPU support.")

# Check if TensorFlow can access the GPU
if gpus:
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        print("\nTensorFlow has access to the GPU.")
    except RuntimeError as e:
        print("\nTensorFlow cannot access the GPU:", e)
else:
    print("\nTensorFlow cannot access the GPU: No GPUs available.")

# Additional tips
print("\nAdditional Tips:")
print("1. Ensure that your GPU is compatible with TensorFlow.")
print("2. Update your GPU drivers and install the correct version of CUDA Toolkit and cuDNN.")
print("3. Check for any error messages in the console and address any issues that they point out.")
print("4. If you are using a virtual environment, ensure that TensorFlow is installed in that environment.")
print("5. Make sure you have installed the TensorFlow version that supports GPU (tensorflow-gpu) if you are using TensorFlow 1.x.")
print("6. If you continue to experience issues, consider seeking help on TensorFlow's official forums or on Stack Overflow.")
