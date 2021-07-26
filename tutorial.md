# Here is a tutorial for RolandoDB in Python

# Installation
Download the module, you can use the folder rolandodb and put it in the python lib folder or if you want,
just use the __init__ file in your source code folder and it will work too.

# Tutorial
Basic test:
```
import rolandodb

select = rolandodb.RDBSelect("testfile.rdb") #File to open, if it doesn't exists, it creates it.
def main():
  print(select.getRawData()) #Get data as raw JSON by reading the given path.
  print(select.getParsedData()) #Get data as parsed JSON (dict).
if __name__ == "__main__":
  main()
```
Output:
```
{}
{}
```
Saving changes:
```
import rolandodb

select = rolandodb.RDBSelect("testfile.rdb") #File to open, if it doesn't exists, it creates it.
def main():
  select.commitChanges() #This method saves changes.
if __name__ == "__main__":
  main()
```
Creation/Get of objects and elements.
```
import rolandodb

select = rolandodb.RDBSelect("testfile.rdb") #File to open, if it doesn't exists, it creates it.
def main():
  select.createObject("testobject")
  select.createElementInObject("testobject","elemname",12313) #last parameter is the value
  print(select.getElementFromObject("testobject","elemname"))
  print(select.getAllElementsFromObjects("testobject")) #It will return a dict.
  select.commitChanges()
if __name__ == "__main__":
  main()
```
Output:
```
12313
{'elemname':12313}
```
Warning about this code: If we open the code again, we are trying to recreate the object, so RolandoDB will throw a ObjectAlreadyExistsError, Also
it will throw a ElementAlreadyExistsError because you are also trying to recreate a element, these methods are used in a few cases, see below for help.

Safe creation of objects and elements:
```
import rolandodb

select = rolandodb.RDBSelect("testfile.rdb") #File to open, if it doesn't exists, it creates it.
def main():
  select.createObjectIfNotExists("testobject")
  select.createElementInObjectIfNotExists("testobject","elemname",12313) #last parameter is the value, if it doesnt exits it will return None.
  print(select.getElementFromObjectIfExists("testobject","elemname")) #
  print(select.getAllElementsFromObjectsIfExists("testobject")) #It will return a dict.
  select.commitChanges()
if __name__ == "__main__":
  main()
```
Output:
```
12313
{'elemname':12313}
```
Deletion of elements and object:
```
import rolandodb

select = rolandodb.RDBSelect("testfile.rdb") #File to open, if it doesn't exists, it creates it.
def main():
  select.createObjectIfNotExists("testobject")
  select.createElementInObjectIfNotExists("testobject","elemname",12313) #last parameter is the value, if it doesnt exits it will return None.
  select.deleteElementFromObject("testobject","elemname")
  select.deleteObject("testobject")
  select.commitChanges()
if __name__ == "__main__":
  main()
```

No output.

Warning: If you use delete methods in objects/elements that do not exist, it will throw a ElementDoesNotExistsError or ObjectDoesNotExistsError.

Safe deletion:
```
import rolandodb

select = rolandodb.RDBSelect("testfile.rdb") #File to open, if it doesn't exists, it creates it.
def main():
  print(select.deleteElementFromObjectIfExists("testobject","elemname")) #if not exists it will return None
  print(select.deleteObjectIfExists("testobject")) #if not exists it will return None
  select.commitChanges()
if __name__ == "__main__":
  main()
```
Output:
```
None
None
```
Refresh and clearing:

If you want to refresh the database if other script/anything changed it you will need this method:
RDBSelect.refreshData()

It will reopen the file and parse it again.
To clear the database use:
RDBSelect.clearDatabase()

It will delete ALL of the data, objects and his elements.

End of tutorial.
