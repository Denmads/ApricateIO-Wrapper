from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import apricatewrapper

@dataclass
class Users:
    api: 'apricatewrapper.ApricateAPI'

    def create_user(self, username: str) -> dict:
        return self.api._post_request(f"/users/{username}/claim")

    def public_user_info(self, username: str) -> dict:
        return self.api._get_request(f"/users/{username}")

    def my_user_info(self) -> dict:
        if not self.api.has_auth_token():
            raise apricatewrapper.MissingAuthTokenException

        return self.api._get_request("/my/user")