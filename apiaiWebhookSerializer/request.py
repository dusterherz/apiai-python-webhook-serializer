import json
from addict import Dict

class Request:
    def __init__(self, data):
        self.__dict__.update(Dict(json.loads(data)))
