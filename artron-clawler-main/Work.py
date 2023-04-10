import json

class Work:
    def __init__(self, wid: str):
        self.wid = wid
        self.basic_info = None

    def set_basic_info(self, basic_info: dict):
        self.basic_info = basic_info

    def save_to_json(self, root_path: str = "./data/"):
        path = root_path + self.wid + ".json"
        # TODO: merge all data into one json file
        with open(path, "w") as f:
            json.dump(self.basic_info, f)

   