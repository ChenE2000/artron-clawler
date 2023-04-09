import json

class Work:
    def __init__(self, wid: str):
        self.wid = wid
        self.basic_info = None

    def _to_dict(self):
        return {
            "wid": self.wid,
            "url": f"https://auction.artron.net/paimai-art{self.wid}",
            "basic_info": self.basic_info
        }

    def set_basic_info(self, basic_info: dict):
        self.basic_info = basic_info

    def save_to_json(self, root_path: str = "./data/"):
        path = root_path + self.wid + ".json"
        # TODO: merge all data into one json file
        with open(path, "w") as f:
            json.dump(self._to_dict(), f)

   