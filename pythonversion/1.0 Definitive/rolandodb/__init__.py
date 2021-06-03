import json
import os
version = "1.0 Definitive"
class ObjectAlreadyExistsError(Exception):
   def __init__(self):
        self.message = "Object already exists in database."
        super().__init__(self.message)
class ObjectDoesntExistsError(Exception):
   def __init__(self):
        self.message = "Object doesn't exists in database."
        super().__init__(self.message)
class ElementDoesntExistsError(Exception):
   def __init__(self):
        self.message = "Element doesn't exists in object."
        super().__init__(self.message)
class ParseError(Exception):
   def __init__(self):
        self.message = "Error happened while parsing JSON, Check the .rdb file and see if it has errors like missing pharentesis."
        super().__init__(self.message)
class RDBSelect:
    def __init__(self,filepath):
        self.filepath = filepath
        try:
            self.file = open(filepath,"r").read()
            if self.file == "":
               open(filepath,"w").write("{}")
               print("Database was empty, now the content is {}.")
               try:    
                   self.data = json.loads(self.file)
               except:  
                   raise ParseError()
            else:
               try:    
                  self.data = json.loads(self.file)
               except:
                  raise ParseError()
        except FileNotFoundError: 
            print("RDB File not found!")
    def getRawData(self):
        return self.file
    def getParsedData(self):
        return self.data
    def getAllElementsFromObject(self,objectname):
        return self.data[objectname]
    def getAllElementsFromObjectIfExists(self,objectname):
        if objectname in self.data:
           return self.data[objectname]
        else:
           pass
    def createObject(self,name):
        if name in self.data:
            raise ObjectAlreadyExistsError()
        else:
            self.data[name] = {}
    def createObjectIfNotExists(self,name):
        if name in self.data:
            return False
        else:
            self.data[name] = {}
            return True
    def deleteObject(self,name):
        if name not in self.data:
            raise ObjectDoesntExistsError()
        else:
            del self.data[name]
    def deleteObjectIfExists(self,name):
        if name not in self.data:
            pass
        else:
            del self.data[name]
    def deleteElementFromObject(self,obj,element):
        del self.data[obj][element]
    def deleteElementFromObjectIfExists(self,obj,element):
        if element in self.data[obj]:
           del self.data[obj][element]
        else:
           pass
    def createElementInObject(self,obj,elmname,val):
        self.data[obj][elmname] = val
    def createElementInObjectIfNotExists(self,obj,elmname,val):
        if elmname in obj:
           pass
        else:
           self.data[obj][elmname] = val
    def getElementFromObject(self,obj,elm):
       if elm in self.data[obj]:
          return self.data[obj][elm]
       else:
          raise ElementDoesntExistsError()
    def getElementFromObjectIfExists(self,obj,elm):
       if elm in self.data[obj]:
          return self.data[obj][elm]
       else:
          pass
    def turnDatabaseListIntoList(self,listToTurn):
       return list(listToTurn)
    def refreshData(self):
        self.file = open(self.filepath,"r").read()
        self.data = json.loads(self.file)
    def clearDatabase(self):
        self.data = {}
    def commitChanges(self):
        toChange = open(self.filepath,"w")
        toChange.truncate()
        toChange.write(json.dumps(self.data,indent = 4))
def createFileIfNotExists(name):
   if os.path.exists(name+".rdb"):
      pass
   else:
      open(name+".rdb","w")
def createFile(name):
   if os.path.exists(name+".rdb"):
      print("File exists.")
   else:
      open(name+".rdb","w")
if __name__ == "__main__":
    print("RolandoDB version is: "+version+".")
