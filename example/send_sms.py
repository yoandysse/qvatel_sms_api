from qvatel.client import QvaTelClient

# Reemplaza 'your_api_token' con tu token de API real
api_token = '66f7f95f5943105842ee3b1d' # Reemplaza esto con tu token de API real
destination = '+34611987283' # Reemplaza esto con un número de teléfono real

# Crea una instancia del cliente
client = QvaTelClient(api_token)

# Envía un SMS
message = 'Hola mundo desde QvaTel'
response = client.send_sms(destination, message)
print(response)
