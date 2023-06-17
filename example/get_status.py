from qvatel.client import QvaTelClient

# Reemplaza 'your_api_token' con tu token de API real
api_token = '66f7f95f5943105842ee3b1d' # Reemplaza esto con tu token de API real
message_id = 'qvatel23479287356' # Reemplaza esto con un ID de mensaje real

# Crea una instancia del cliente
client = QvaTelClient(api_token)

# Obtiene el estado de un mensaje
status = client.get_message_status(message_id)
print(status)
