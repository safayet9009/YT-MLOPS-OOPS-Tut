'''
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "Hello, " + self.name
  def welcome(self):
    message=self.greet()
    print(message +'! welcome to my website')


p1=Person('Tobias')    
p1.welcome()
'''
'''
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person('shafayet',25)
p1.age=40
del p1.age
print(p1.name)
'''
'''
class person:
    species='human'

    def __init__(self,name):
        self.name=name

p1=person("emily")
p2=person('tobias')

print(p1.species)
print(p2.species)

print(p1.name)
'''
'''
class person:
    lastname='Jackson'

    def __init__(self,name):
        self.name=name
        
p1=person('Emil')
p2=person('Tobias')
print(p1.lastname)

person.lastname='Hansen'
print(p1.lastname)
print(person.lastname)
print(p2.lastname)
print(p1.name)
'''
'''
class calculator:
    def add(self,a,b):
        return a+b
    def mul(self,a,b):
        return a*b
calc=calculator()

print(calc.add(5,3)) 
print(calc.mul(23,4))
'''
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def greet(self):
        return f'{self.name} is {self.age} years old'   
p1=person("John", 30)

print(p1.greet())