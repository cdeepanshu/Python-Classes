def hello (name):
    print("Hello ",name)

hello("Deepanshu")
hello("Rohit")
def add(x=0,y=0):
    return(x+y)
sum1=add (100,100)
print(sum1)
sum2=add(230,139)
print(sum2)
sum3=add()
print(sum3)
def student(name,*score):
    print(name)
    print(score)
student("jon",55,80,36,67)    
