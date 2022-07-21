import json

class DbInterface:
    def __init__(self):
        self.dataFile = "./data.json"
        file = open(self.dataFile, "r")
        fileContents = file.read()
        self.data = json.loads(fileContents)
        # print(self.data)
