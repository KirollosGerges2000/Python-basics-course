#lab14 "Python classes and objects"
#scripted by Eng/Kirollos Gerges

from Employee import Employee
from Employee import student

employee1=Employee("kirollos","24","self_learning",False)
employee2=Employee("Eslam","26","sw enginner",True)

print(employee1.age)
print(employee2.ismanager)

student1=student("Fadii","22",3.7)
student2=student("Salah","25",3.5)

print(student1.gpa)
print(student2.name)