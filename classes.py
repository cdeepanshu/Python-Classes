class Person:
    def __init__(self,id):
        self.id=id
        print("constructor is called")
    def __del__(self):
        print(self.id,"Destructor is called")
    def fullname(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printfullname(self):
        print(self.fname," ",self.lname)

personname=Person(5)
personname.fullname("Deepanshu","Chauhan")
personname.printfullname()
personname.__del__()  
        
