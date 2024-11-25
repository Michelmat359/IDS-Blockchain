import hashlib

def generate_hash(data):
    """Genera un hash único para los datos usando SHA-256."""
    encoded_data = str(data).encode('utf-8')
    return hashlib.sha256(encoded_data).hexdigest()
