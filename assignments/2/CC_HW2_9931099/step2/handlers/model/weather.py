import json


class Weather:
    def __init__(self, min_temp, max_temp) -> None:
        self.minT= min_temp
        self.maxT = max_temp

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)