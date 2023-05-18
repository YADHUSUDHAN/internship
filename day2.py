'''def display(fname,lname):
    print("first name : ",fname)
    print("last name : ",lname)
display("yadhu","sudhan")

def display(fname,lname):
    print("first name : ",fname)
    print("last name : ",lname)
display(fname = 'yadhu',lname = 'sudhan')

'''
'''

def add(*num):
    result = 0
    for i in num:
        result = result + i
    print(result)
add(3,4,)

'''


'''
def fullame(**kwargs):
    for k,v in kwargs.items():
        print(k,v)
fullame(fname = 'yadhu',lname = 'sudhan'  )


'''


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p = Person('yadhu',21)
print(p.name)
print(p.age)