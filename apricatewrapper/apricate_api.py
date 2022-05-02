import requests
from apricatewrapper.endpoints import Information, Metrics

class MissingAuthTokenException(Exception):
    pass

class ApricateAPI:
    
    base_url = 'https://apricate.io/api'
    auth_token: str = None

    def __init__(self):
        self.information = Information(self)
        self.metrics = Metrics(self)

    def set_token(self, token):
        self.auth_token = token

    def __headers(self):
        return {'Authorization': f'Bearer {self.auth_token}'} if self.auth_token is not None else None

    def _get_request(self, endpoint: str):
        url = self.base_url + endpoint
        header = self.__headers()
        r = requests.get(url, headers=header)
        return r.json()

    def _post_request(self, endpoint: str, data: dict):
        url = self.base_url + endpoint
        header = self.__headers()
        r = requests.post(url, headers=header, data=data)
        return r.json()

    def _patch_request(self, endpoint: str, data: dict):
        url = self.base_url + endpoint
        header = self.__headers()
        r = requests.patch(url, headers=header, data=data)
        return r.json()

    def _put_request(self, endpoint: str):
        url = self.base_url + endpoint
        header = self.__headers()
        r = requests.post(url, headers=header)
        return r.json()

    def _delete_request(self, endpoint: str):
        url = self.base_url + endpoint
        header = self.__headers()
        r = requests.delete(url, headers=header)
        return r.json()

    