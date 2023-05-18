'''

class Person(object):

    def __init__(self,name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def isEmployee(self):
        return False
    
class Employee(Person):
    def isEmployee(self):
        return True
emp = Person('geek1')
print(emp.getName(),emp.isEmployee())
emp = Employee('geek1')
print(emp.getName(),emp.isEmployee())

'''

'''

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print('Drive')

class Boat:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print('Sail')
    
class Plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print('Fly')
car1 = Car('Ford','Mustang')
boat1 = Boat('Ibiza','Touring 4')
plane1 = Plane('Boeing','747')

for x in (car1,boat1,plane1):
    x.move()

'''


'''

import cal
print(cal.add(3,7))
print(cal.subtract(3,7))

'''

