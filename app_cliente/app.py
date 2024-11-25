from blockchain import BlockchainManager
from mongodb_connector import MongoDBManager
from utils import generate_hash

# Configuración inicial
blockchain_url = "http://127.0.0.1:7545"
blockchain_manager = BlockchainManager(blockchain_url)
mongodb_manager = MongoDBManager()

def save_data(data):
    """Proceso principal para guardar datos."""
    # Generar hash de los datos
    data_hash = generate_hash(data)
    print(f"Hash generado: {data_hash}")

    # Registrar el hash en la blockchain
    tx_hash = blockchain_manager.register_hash(data_hash)
    print(f"Hash registrado en blockchain. Transacción: {tx_hash}")

    # Guardar los datos en MongoDB
    document = {
        "data": data,
        "hash": data_hash,
        "blockchain_tx": tx_hash
    }
    record_id = mongodb_manager.save_data("documents", document)
    print(f"Datos guardados en MongoDB con ID: {record_id}")

if __name__ == "__main__":
    # Ejemplo de datos
    example_data = {
        "name": "Ejemplo",
        "value": 42,
        "timestamp": "2024-11-24T12:00:00Z"
    }

    save_data(example_data)
