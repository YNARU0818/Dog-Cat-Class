import tensorflow as tf

model_path = r'c:\Users\subin\github\Dog-Cat-Class\best_model_xception.keras'
model = tf.keras.models.load_model(model_path)

model.summary()
print("Input shape:", model.input_shape)
print("Output shape:", model.output_shape)
