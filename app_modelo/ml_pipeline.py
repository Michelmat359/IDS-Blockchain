import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.losses import MeanSquaredError
from tensorflow.keras.metrics import MeanAbsoluteError

import numpy as np
import os

MODEL_PATH = "complex_model.h5"

def initialize_pipeline():
    """Crea o carga un modelo de red neuronal para regresión."""
    if os.path.exists(MODEL_PATH):
        print("Cargando modelo existente...")
        model = tf.keras.models.load_model(
            MODEL_PATH,
            custom_objects={
                "mse": MeanSquaredError(),
                "mae": MeanAbsoluteError()
            }
        )
    else:
        print("Creando y entrenando un modelo nuevo...")
        model = create_and_train_model()
        model.save(MODEL_PATH)
    return model

def create_and_train_model():
    """Crea y entrena un modelo de red neuronal."""
    # Crear datos de ejemplo
    np.random.seed(42)
    X_train = np.random.rand(1000, 1) * 100  # Datos de entrada (0 a 100)
    y_train = 2.5 * X_train + np.random.randn(1000, 1) * 5  # Relación lineal con ruido

    # Crear el modelo
    model = Sequential([
        Dense(64, activation='relu', input_shape=(1,)),
        Dense(32, activation='relu'),
        Dense(1)  # Capa de salida para regresión
    ])

    # Compilar el modelo
    model.compile(optimizer='adam', loss=tf.keras.losses.MeanSquaredError(),
                  metrics=[tf.keras.metrics.MeanAbsoluteError()])

    # Entrenar el modelo
    model.fit(X_train, y_train, epochs=50, batch_size=32, verbose=1)

    return model

def predict(data):
    """Predice el resultado para nuevos datos."""
    model = tf.keras.models.load_model(MODEL_PATH)
    return model.predict(data)
