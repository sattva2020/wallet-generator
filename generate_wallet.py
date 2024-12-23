import secrets
from mnemonic import Mnemonic
from eth_account import Account
import base58
import yaml
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

def generate_password(length=12):
    return secrets.token_hex(length // 2)

class WalletGenerator:
    def __init__(self, settings_path='settings.yaml'):
        self.mnemo = Mnemonic("english")
        with open(settings_path, 'r') as file:
            self.settings = yaml.safe_load(file)

    def generate_mnemonic(self):
        return self.mnemo.generate(strength=256)

    def generate_eth_wallet(self):
        """Generate Ethereum wallet with unique mnemonic"""
        mnemonic = self.generate_mnemonic()
        Account.enable_unaudited_hdwallet_features()
        account = Account.from_mnemonic(mnemonic)
        
        return {
            'mnemonic': mnemonic,
            'address': account.address,
            'private_key': account.key.hex()
        }

    def generate_sol_wallet(self):
        """Generate Solana wallet with unique mnemonic"""
        mnemonic = self.generate_mnemonic()  # Отдельная мнемоника для Solana
        private_key = ec.generate_private_key(ec.SECP256K1())
        public_key = private_key.public_key()
        
        private_bytes = private_key.private_numbers().private_value.to_bytes(32, byteorder='big')
        public_bytes = public_key.public_bytes(
            encoding=serialization.Encoding.X962,
            format=serialization.PublicFormat.UncompressedPoint
        )
        
        return {
            'mnemonic': mnemonic,  # Используем уникальную мнемонику
            'address': base58.b58encode(public_bytes).decode(),
            'private_key': base58.b58encode(private_bytes).decode()
        }

    def generate_wallets(self):
        eth_wallet = self.generate_eth_wallet()
        sol_wallet = self.generate_sol_wallet()
        
        password = self.settings['PASSWORD_WALLET'] if not self.settings['RANDOM_PASSWORDS'] else generate_password(self.settings['PASSWORD_LENGTH'])
        
        return {
            'eth_mnemonic': eth_wallet['mnemonic'],
            'eth_address': eth_wallet['address'],
            'eth_private_key': eth_wallet['private_key'],
            'sol_mnemonic': sol_wallet['mnemonic'],
            'sol_address': sol_wallet['address'],
            'sol_private_key': sol_wallet['private_key'],
            'wallet_password': password
        }

if __name__ == "__main__":
    # Пример использования
    generator = WalletGenerator()
    
    # Генерация новых кошельков
    wallets = generator.generate_wallets()
    print("\nСгенерированные кошельки:")
    print(f"Мнемоника ETH: {wallets['eth_mnemonic']}")
    print(f"Адрес Ethereum: {wallets['eth_address']}")
    print(f"Мнемоника Solana: {wallets['sol_mnemonic']}")
    print(f"Адрес Solana: {wallets['sol_address']}")
    print(f"Пароль кошелька: {wallets['wallet_password']}")
