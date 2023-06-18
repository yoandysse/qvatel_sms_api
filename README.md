# QvaTel Python Library

Esta librería proporciona una interfaz de Python para interactuar con la API de SMS de QvaTel

## Funciones

* Enviar mensajes SMS.
* Obtener el estado de los mensajes.
* Consultar el balance de la cuenta.

## Requisitos

- Python 3.6 o superior.
- Una cuenta de QvaTel con un API token de SMS.

## Instalación

Instala la librería usando pip:

```
pip install qvatel-sms-api

```

## Uso

Aquí hay un ejemplo básico de cómo usar la librería para enviar un SMS, obtener el estado de un mensaje y consultar el balance de la cuenta:

```python
from qvatel.client import QvaTelClient

# Inicializa el cliente con tu API token
client = QvaTelClient('your_api_token_here')

# Envía un SMS
destination = '+5352942387'
message = 'Hola mundo desde QvaTel'
response = client.send_sms(destination, message)
print(response)

# Obtiene el estado de un mensaje
message_id = 'your_message_id_here'
status = client.get_message_status(message_id)
print(status)

# Obtiene el balance de la cuenta
balance = client.get_account_balance()
print(balance)
```

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue si encuentras un bug o tienes una solicitud de función.
