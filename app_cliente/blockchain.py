from web3 import Web3

class BlockchainManager:
    def __init__(self, rpc_url):
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        if not self.web3.is_connected():
            raise ConnectionError("No se pudo conectar a la blockchain.")
        self.account = self.web3.eth.accounts[0]  # Asegúrate de tener cuentas en tu blockchain.

    def register_hash(self, data_hash):
        """Registra un hash en la blockchain."""
        transaction = {
            'from': self.account,
            'to': self.account,
            'value': 0,
            'gas': 100000,
            'gasPrice': self.web3.to_wei('1', 'gwei'),
            'data': self.web3.to_hex(text=data_hash)
        }
        tx_hash = self.web3.eth.send_transaction(transaction)
        return tx_hash.hex()

    def get_registered_hash(self, tx_hash):
        """Obtiene el hash registrado usando el hash de transacción."""
        receipt = self.web3.eth.get_transaction(tx_hash)
        return self.web3.to_text(hexstr=receipt.input)
