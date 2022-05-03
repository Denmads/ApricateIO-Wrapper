from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import apricatewrapper

@dataclass
class Locations:
    api: 'apricatewrapper.ApricateAPI'

    def islands(self) -> dict:
        return self.api._get_request("/islands")

    def specific_island(self, symbol: str) -> dict:
        return self.api._get_request(f"/islands/{symbol}")

    def regions(self) -> dict:
        return self.api._get_request("/regions")

    def specific_region(self, symbol: str) -> dict:
        return self.api._get_request(f"/regions/{symbol}")

    def my_locations(self) -> dict:
        if not self.api.has_auth_token():
            raise apricatewrapper.MissingAuthTokenException

        return self.api._get_request("/my/locations")
    
    def my_specific_location(self, symbol: str) -> dict:
        if not self.api.has_auth_token():
            raise apricatewrapper.MissingAuthTokenException

        return self.api._get_request(f"/my/locations/{symbol}")

    def my_nearby_locations(self) -> dict:
        if not self.api.has_auth_token():
            raise apricatewrapper.MissingAuthTokenException

        return self.api._get_request("/my/nearby-locations")