from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import apricatewrapper

@dataclass
class Metrics:
    api: 'apricatewrapper.ApricateAPI'

    def users(self) -> dict:
        return self.api._get_request("/users")

    def metrics(self) -> dict:
        return self.api._get_request("/metrics")