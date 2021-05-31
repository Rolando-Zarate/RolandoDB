import json
version = "1.0 Beta"
class ObjectAlreadyExistsError(Exception):
   def __init__(self):
        self.message = "Object already exists in database."
        super().__init__(self.message)
class ObjectDoesntExistsError(Exception):
   def __init__(self):
        self.message = "Object doesn't exists in database."
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
    def getDataAsDict(self):
        return self.data
    def getObject(self,objectname):
        return self.data[objectname]
    def createObject(self,name):
        if name in self.data:
            raise ObjectAlreadyExistsError()
        else:
            self.data[name] = {}
    def createObjectIfNotExists(self,name):
        if name in self.data:
            pass
        else:
            self.data[name] = {}
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
    def createElementInObject(self,obj,elmname,val):
        self.data[obj][elmname] = val
    def createElementInObjectIfNotExists(self,obj,elmname,val):
        if elmname in obj:
           pass
        else:
           self.data[obj][elmname] = val
    def refreshData(self):
        self.file = open(self.filepath,"r").read()
    def commitChanges(self):
        toChange = open(self.filepath,"w")
        toChange.truncate()
        toChange.write(json.dumps(self.data,indent = 4))    
if __name__ == "__main__":
    print("RolandoDB version is: "+version+".")
