#Lab 20 [static and class method]
#scripted by:
#Eng/Kirollos Gerges

from datetime import date

class student:
    def __init__(self,name,age,gpa):
        self.name=name
        self.age=age
        self.gpa=gpa

#class method to change the behavior of classes
@classmethod
def initFromBirthyear(cls,name,birthyear):
    return cls(name,date.today().year-birthyear)

#student33=initFromBirthyear("kirollos",2000)

#student33.describe()

#print(dir(student33))


@staticmethod
def add22(x):
    return x+10

print(add22(2))