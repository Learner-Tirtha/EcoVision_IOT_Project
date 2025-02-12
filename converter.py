import tensorflow as tf

# Load the Keras model
model_path = "waste_classification_mobilenetv2_model.h5"
model = tf.keras.models.load_model(model_path)

# Initialize the TFLite Converter
converter = tf.lite.TFLiteConverter.from_keras_model(model)

# Optional: Enable optimizations for smaller and faster models
converter.optimizations = [tf.lite.Optimize.DEFAULT]

# Optional: Specify supported operations (if targeting specific hardware)
# converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS,  # Default operations
#                                        tf.lite.OpsSet.SELECT_TF_OPS]   # Enable TensorFlow ops if needed

# Optional: Enable quantization (e.g., dynamic range quantization)
# converter.representative_dataset = your_dataset_function  # Provide representative data for quantization
# converter.target_spec.supported_types = [tf.float16]      # Example: Float16 quantization

# Convert the model to TensorFlow Lite format
tflite_model = converter.convert()

# Save the TensorFlow Lite model
tflite_model_path = "waste_classification_model.tflite"
with open(tflite_model_path, "wb") as f:
    f.write(tflite_model)

print(f"Model successfully converted to TensorFlow Lite format and saved as '{tflite_model_path}'")
