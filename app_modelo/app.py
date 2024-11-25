from blockchain import BlockchainManager
from mongodb_connector import MongoDBManager
from utils import generate_hash
from ml_pipeline import initialize_pipeline
import numpy as np

# Configuración inicial
blockchain_url = "http://127.0.0.1:7545"
blockchain_manager = BlockchainManager(blockchain_url)
mongodb_manager = MongoDBManager()

# Inicializar el pipeline de ML
ml_pipeline = initialize_pipeline()


def consume_data(query):
    """Proceso principal para consumir datos."""
    # Obtener datos desde MongoDB
    document = mongodb_manager.get_data("documents", query)
    if not document:
        raise ValueError("No se encontraron datos para la consulta proporcionada.")

    data = document["data"]
    registered_hash = document["hash"]
    tx_hash = document["blockchain_tx"]

    # Validar el hash
    calculated_hash = generate_hash(data)
    print(f"Hash calculado: {calculated_hash}")
    print(f"Hash registrado: {registered_hash}")

    if calculated_hash != registered_hash:
        raise ValueError("El hash calculado no coincide con el registrado en MongoDB.")

    # Validar hash en blockchain
    stored_hash = blockchain_manager.get_registered_hash(tx_hash)
    print(f"Hash recuperado de blockchain: {stored_hash}")

    if calculated_hash != stored_hash:
        raise ValueError("El hash recuperado de la blockchain no coincide con los datos.")

    print("Datos validados correctamente.")

    # Procesar los datos con el modelo ML
    input_data = np.array([[data["value"]]])  # Convertir el valor de ejemplo en un formato utilizable
    prediction = ml_pipeline.predict(input_data)
    print(f"Predicción generada: {prediction}")

    return prediction


if __name__ == "__main__":
    # Ejemplo de consulta
    query = {"data.name": "Ejemplo"}
    try:
        result = consume_data(query)
        print(f"Resultado final: {result}")
    except Exception as e:
        print(f"Error: {e}")
