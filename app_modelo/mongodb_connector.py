from pymongo import MongoClient

class MongoDBManager:
    def __init__(self, db_url="mongodb://localhost:27017/", db_name="data_storage"):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]

    def save_data(self, collection_name, data):
        """Guarda datos en una colección específica."""
        collection = self.db[collection_name]
        result = collection.insert_one(data)
        return result.inserted_id

    def get_data(self, collection_name, query):
        """Obtiene datos desde una colección específica."""
        collection = self.db[collection_name]
        return collection.find_one(query)
