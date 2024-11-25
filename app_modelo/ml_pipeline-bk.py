import numpy as np
from sklearn.linear_model import LinearRegression

class MLPipeline:
    def __init__(self):
        """Inicialización del modelo ML."""
        self.model = LinearRegression()

    def train_model(self, X, y):
        """Entrena el modelo con datos de ejemplo."""
        self.model.fit(X, y)

    def predict(self, X):
        """Genera predicciones con los datos proporcionados."""
        return self.model.predict(X)

# Inicialización del modelo con datos de entrenamiento ficticios
def initialize_pipeline():
    pipeline = MLPipeline()
    # Datos de ejemplo para entrenar el modelo
    X_train = np.array([[1], [2], [3], [4]])
    y_train = np.array([2, 4, 6, 8])
    pipeline.train_model(X_train, y_train)
    return pipeline
