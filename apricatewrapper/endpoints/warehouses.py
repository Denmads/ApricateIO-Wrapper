from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import apricatewrapper

@dataclass
class Warehouses:
    api: 'apricatewrapper.ApricateAPI'

    def my_warehouses(self) -> dict:
        if not self.api.has_auth_token():
            raise apricatewrapper.MissingAuthTokenException

        return self.api._get_request("/my/warehouses")

    def my_specific_warehouse(self, symbol: str) -> dict:
        if not self.api.has_auth_token():
            raise apricatewrapper.MissingAuthTokenException

        return self.api._get_request(f"/my/warehouses/{symbol}")