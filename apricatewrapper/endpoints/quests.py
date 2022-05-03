from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import apricatewrapper

@dataclass
class Quests:
    api: 'apricatewrapper.ApricateAPI'

    def my_contracts(self) -> dict:
        if not self.api.has_auth_token():
            raise apricatewrapper.MissingAuthTokenException

        return self.api._get_request("/my/contracts")

    def my_specific_contract(self, id: int) -> dict:
        if not self.api.has_auth_token():
            raise apricatewrapper.MissingAuthTokenException

        return self.api._get_request(f"/my/contracts/{id}")