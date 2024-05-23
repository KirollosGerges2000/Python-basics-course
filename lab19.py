#Lab 19 [public and private class]
#scripted by:
#Eng/Kirollos Gerges

#private class
class Employee:
    def __init__(self,name,age,depertment,is_manager):
        self.__name=name
        self.__age=age
        self.__depertment=depertment
        self.__manager=is_manager

#public class
class Employee:
    def __init__(self,name,age,depertment,is_manager):
        self.name=name
        self.age=age
        self.depertment=depertment
        self.manager=is_manager
