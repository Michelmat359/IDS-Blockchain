from flask import Flask, request, jsonify
from flask_cors import CORS  # Importa Flask-CORS
from blockchain import BlockchainManager
from mongodb_connector import MongoDBManager
from utils import generate_hash
from ml_pipeline import initialize_pipeline
import numpy as np


# Configuración
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
blockchain_url = "http://127.0.0.1:7545"
blockchain_manager = BlockchainManager(blockchain_url)
mongodb_manager = MongoDBManager()
ml_pipeline = initialize_pipeline()


@app.route('/store', methods=['POST'])
def store_data():
    """Endpoint para almacenar datos."""
    try:
        # Obtener datos del request
        data = request.json
        if not data:
            return jsonify({"error": "No se enviaron datos"}), 400

        # Generar hash y registrar en blockchain
        data_hash = generate_hash(data)
        tx_hash = blockchain_manager.register_hash(data_hash)

        # Guardar en MongoDB
        document = {
            "data": data,
            "hash": data_hash,
            "blockchain_tx": tx_hash
        }
        record_id = mongodb_manager.save_data("documents", document)

        return jsonify({
            "message": "Datos almacenados con éxito",
            "record_id": str(record_id),
            "hash": data_hash,
            "transaction": tx_hash
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/retrieve', methods=['GET'])
def retrieve_data():
    """Endpoint para recuperar y validar datos."""
    try:
        # Obtener el filtro de la consulta
        query = request.args.to_dict()
        if not query:
            return jsonify({"error": "No se proporcionó un filtro"}), 400

        # Ajustar consulta para MongoDB si tiene prefijo como 'data.'
        query = {key.replace("data.", "data."): value for key, value in query.items()}

        # Recuperar datos de MongoDB
        document = mongodb_manager.get_data("documents", query)
        if not document:
            return jsonify({"error": "No se encontraron datos para el filtro dado"}), 404

        data = document["data"]
        registered_hash = document["hash"]
        tx_hash = document["blockchain_tx"]

        # Validar el hash
        calculated_hash = generate_hash(data)
        if calculated_hash != registered_hash:
            return jsonify({"error": "El hash calculado no coincide con el registrado en MongoDB"}), 400

        # Validar hash en blockchain
        stored_hash = blockchain_manager.get_registered_hash(tx_hash)
        if calculated_hash != stored_hash:
            return jsonify({"error": "El hash recuperado de blockchain no coincide con los datos"}), 400

        # Conversión de datos a valores numéricos
        try:
            value = float(data["value"])  # Convierte el valor a numérico
        except ValueError:
            return jsonify({"error": "El campo 'value' no es numérico."}), 400

        # Ejecutar el modelo ML
        input_data = np.array([[value]])  # Asegúrate de que el modelo reciba un arreglo numérico
        prediction = ml_pipeline.predict(input_data)

        return jsonify({
            "message": "Datos validados y procesados con éxito",
            "prediction": prediction.tolist(),
            "data": data
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
