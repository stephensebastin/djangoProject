import json
import os

from djangoProject.settings import BASE_DIR


class Singleton:
    configurationsData = ""

    @staticmethod
    def getConfigurations():
        if Singleton.configurationsData == "":
            Singleton()
        return Singleton.configurationsData

    def __init__(self):
        if Singleton.configurationsData != "":
            raise Exception("This class is a singleton class !")
        else:
            json_data = os.path.join(BASE_DIR, 'static', "configurations.json")
            fileData = open(json_data, 'r')
            Singleton.configurationsData = json.load(fileData)
            fileData.close()
