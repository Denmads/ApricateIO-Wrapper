from dataclasses import dataclass

@dataclass
class Metrics:
    api: any

    def users(self) -> dict:
        return self.api._get_request("/users")

    def metrics(self) -> dict:
        return self.api._get_request("/metrics")