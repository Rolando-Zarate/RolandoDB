import json
import os

version = "1.0 beta 05 07 2021"


class RolandoDBException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class ObjectAlreadyExistsError(RolandoDBException):
    def __init__(self):
        self.message = "Object already exists in database."
        super().__init__(self.message)


class ObjectDoesNotExistsError(RolandoDBException):
    def __init__(self):
        self.message = "Object does not exists in database."
        super().__init__(self.message)


class ElementDoesNotExistsError(RolandoDBException):
    def __init__(self):
        self.message = "Element does not exists in object."
        super().__init__(self.message)


class RDBSelect:
    def __init__(self, filepath):
        self.filepath = filepath
        if os.path.exists(self.filepath):
            with open(self.filepath) as file:
                try:
                    self.data = json.load(file) 
                except json.decoder.JSONDecodeError as e:
                    raise e
        else:
            newfile = open(self.filepath,"w")
            newfile.write("{}")
            newfile.close()
            with open(self.filepath) as file:
                try:
                    self.data = json.load(file) 
                except json.decoder.JSONDecodeError as e:
                    raise e


    def getRawData(self):
        with open(self.filepath) as file:
            return file.read()

    def getParsedData(self):
        return self.data

    def getAllElementsFromObject(self, objectname):
        if objectname in self.data:
            return self.data[objectname]
        else:
            raise ObjectDoesNotExistsError()
    def getAllElementsFromObjectIfExists(self, objectname):
        if objectname in self.data:
            return self.data[objectname]
        else:
            return None

    def createObject(self, name):
        if name in self.data:
            raise ObjectAlreadyExistsError()
        else:
            self.data[name] = {}

    def createObjectIfNotExists(self, name):
        if name in self.data:
            return None
        else:
            self.data[name] = {}
            return True

    def deleteObject(self, name):
        try:
            del self.data[name]
        except KeyError:
            raise ObjectDoesNotExistsError()

    def deleteObjectIfExists(self, name):
        if name not in self.data:
            pass
        else:
            del self.data[name]

    def deleteElementFromObject(self, obj, element):
        del self.data[obj][element]

    def deleteElementFromObjectIfExists(self, obj, element):
        if obj in self.data and element in self.data[obj]:
            del self.data[obj][element]
        else:
            return None

    def createElementInObject(self, obj, elmname, val):
        self.data[obj][elmname] = val

    def createElementInObjectIfNotExists(self, obj, elmname, val):
        if elmname in obj:
            return None
        else:
            self.data[obj][elmname] = val

    def getElementFromObject(self, obj, elm):
        try:
            return self.data[obj][elm]
        except KeyError:
            raise ElementDoesNotExistsError()

    def getElementFromObjectIfExists(self, obj, elm):
        if elm in self.data[obj]:
            return self.data[obj][elm]
        else:
            return None

    def refreshData(self):
        with open(self.filepath, "r") as file:
            self.data = json.loads(file)

    def clearDatabase(self):
        self.data = {}

    def commitChanges(self):
        with open(self.filepath, "w") as toChange:
            toChange.truncate()
            toChange.write(json.dumps(self.data))


if __name__ == "__main__":
    print("RolandoDB version is: " + version + ".")
