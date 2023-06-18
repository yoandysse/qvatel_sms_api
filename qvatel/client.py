import requests


class QvaTelClient:
    """
    Cliente para interactuar con la API de QvaTel.
    """

    def __init__(self, api_token):
        """
        Inicializa el cliente de QvaTel.

        :param api_token: El token de la API de QvaTel.
        """
        self.api_token = api_token
        self.base_url = "https://qvatel.com/api"

    def send_sms(self, destination, message):
        """
        Envía un mensaje SMS a través de la API de QvaTel.

        :param destination: Número de teléfono del destinatario, incluido el código del país.
        :param message: Contenido del mensaje SMS a enviar.
        :return: Respuesta de la API en formato JSON.
        """
        if not isinstance(destination, str) or not isinstance(message, str):
            raise ValueError("Destination and message must be strings")

        url = f"{self.base_url}/sms/send"
        payload = {
            "api_token": self.api_token,
            "destino": destination,
            "mensaje": message
        }
        try:
            response = requests.post(url, data=payload, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            raise Exception(f"Error sending SMS: {e}")
        return response.json()

    def get_message_status(self, message_id):
        """
        Obtiene el estado de un mensaje SMS enviado a través de la API de QvaTel.

        :param message_id: ID del mensaje para el cual se desea obtener el estado.
        :return: Respuesta de la API en formato JSON.
        """
        url = f"{self.base_url}/sms/report-status"
        payload = {
            "api_token": self.api_token,
            "id_msg": message_id
        }
        try:
            response = requests.get(url, params=payload, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            raise Exception(f"Error getting message status: {e}")
        return response.json()

    def get_account_balance(self):
        """
        Obtiene el balance de la cuenta de QvaTel asociada al token de la API.

        :return: Respuesta de la API en formato JSON.
        """
        url = f"{self.base_url}/account/balance"
        payload = {
            "api_token": self.api_token
        }
        try:
            response = requests.get(url, params=payload, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            raise Exception(f"Error getting account balance: {e}")
        return response.json()
