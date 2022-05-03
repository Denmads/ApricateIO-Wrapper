import requests
from apricatewrapper.endpoints import Information, Metrics, Locations, Warehouses, Users, Quests

class MissingAuthTokenException(Exception):
    pass

class ApricateAPI:

    def __init__(self):
        self.base_url = 'https://apricate.io/api'
        self._auth_token: str = None
        self.information = Information(self)
        self.locations = Locations(self)
        self.metrics = Metrics(self)
        self.quests = Quests(self)
        self.users = Users(self)
        self.warehouses = Warehouses(self)

    def set_token(self, token):
        self._auth_token = token

    def has_auth_token(self) -> bool:
        return self._auth_token is not None

    def __headers(self):
        return {'Authorization': f'Bearer {self._auth_token}'} if self._auth_token is not None else None

    def _get_request(self, endpoint: str) -> dict:
        url = self.base_url + endpoint
        header = self.__headers()
        r = requests.get(url, headers=header)
        return r.json()

    def _post_request(self, endpoint: str, data: dict = None) -> dict:
        url = self.base_url + endpoint
        header = self.__headers()
        r = requests.post(url, headers=header, data=data)
        return r.json()

    def _patch_request(self, endpoint: str, data: dict = None) -> dict:
        url = self.base_url + endpoint
        header = self.__headers()
        r = requests.patch(url, headers=header, data=data)
        return r.json()

    def _put_request(self, endpoint: str) -> dict:
        url = self.base_url + endpoint
        header = self.__headers()
        r = requests.post(url, headers=header)
        return r.json()

    def _delete_request(self, endpoint: str) -> dict:
        url = self.base_url + endpoint
        header = self.__headers()
        r = requests.delete(url, headers=header)
        return r.json()

    