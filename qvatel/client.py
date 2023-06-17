import requests


class QvaTelClient:

    def __init__(self, api_token):
        self.api_token = api_token
        self.base_url = "https://qvatel.com/api"

    def send_sms(self, destination, message):
        url = f"{self.base_url}/sms/send"
        payload = {
            "api_token": self.api_token,
            "destino": destination,
            "mensaje": message
        }
        response = requests.post(url, data=payload)
        return response.json()

    def get_message_status(self, message_id):
        url = f"{self.base_url}/sms/report-status"
        payload = {
            "api_token": self.api_token,
            "id_msg": message_id
        }
        response = requests.get(url, params=payload)
        return response.json()

    def get_account_balance(self):
        url = f"{self.base_url}/account/balance"
        payload = {
            "api_token": self.api_token
        }
        response = requests.get(url, params=payload)
        return response.json()
