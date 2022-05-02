from dataclasses import dataclass

@dataclass
class Information:
    api: any

    def about(self, extension: str = None) -> dict:
        endpoint = "/about" if extension is None else f"/about{extension}"
        return self.api._get_request(endpoint)

    def about_sizes(self) -> dict:
        return self.about("/sizes")

    def about_magic(self) -> dict:
        return self.about("/magic")

    def about_plants(self) -> dict:
        return self.about("/plants")

    def about_world(self) -> dict:
        return self.about("/world")