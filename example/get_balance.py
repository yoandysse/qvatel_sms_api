from qvatel.client import QvaTelClient

# Reemplaza 'your_api_token' con tu token de API real
api_token = '66f7f95f5943105842ee3b1d' # Reemplaza esto con tu token de API real

# Crea una instancia del cliente
client = QvaTelClient(api_token)

# Obtiene el balance de la cuenta
balance = client.get_account_balance()
print(balance)

