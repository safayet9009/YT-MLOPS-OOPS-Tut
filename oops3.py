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


'''
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def greet(self):
        return f'{self.name} is {self.age} years old'   
p1=person("John", 30)

print(p1.greet())
'''
'''
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def celebrate_brtday(self):
        self.age+=1
        print (f"Happy birthday {self.name},u r now {self.age} years old")

p1=person('safayet',25)

p1.celebrate_brtday()
p1.celebrate_brtday()
'''

'''

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

p1=person("Shafayet", 25)

print(p1)

'''


#encapsulation

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age

# p1=person('Emil',25)

# print(p1.name)
# #print(p1.__age)
# print(p1._person__age)




# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age

#     def get_age(self):
#         return self.__age
    
# p1=person('emil', 30)
# print(p1.get_age())


#setter method

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age

#     def get_age(self):
#         return self.__age
    
#     def set_age(self,age):
#         if age>0:
#             self.__age=age

#         else:
#             print('Age must be positive')

# p1=person('Tobias', 25)

# print(p1.get_age())

# p1.set_age(30)
# print(p1.get_age())


#setter+getter+encapsulation

# class student:
#     def __init__(self, name):
#         self.name=name
#         self.__grade=0

#     def set_grade(self,grade):
#         if 0<= grade <=100:
#             self.__grade=grade

#         else:
#             print('grade must be between 0 and 100')

#     def get_grade(self):
#         return self.__grade
    
#     def get_status(self):
#         if self.__grade >=60:
#             return 'passed'
        
#         else:
#             return 'failed'
        
# student=student('Emil')

# student.set_grade(85)

# print(student.get_grade())
# print(student.get_status())

#private methods

# class calculator:
#     def __init__(self):
#         self.result=0

#     def __validate(self,num):
#         if not isinstance(num,(int,float)):
#             return False
#         return True
    
#     def add(self,num):
#         if self.__validate(num):
#             self.result+=num

#         else:
#             print('invalid number')

# calc=calculator()
# calc.add(10)
# calc.add(5)
# print(calc.result)


#static method

# class mathhelper:
#     @staticmethod
#     def square(num):
#         return num * num
    

# print(mathhelper.square(5))


# class user:
#     @staticmethod
#     def is_validate_age(age):
#         if isinstance(age,int) and age>=18:
#             return True
#         return False
    
# print(user.is_validate_age(20))
# print(user.is_validate_age(15))



#inheritance

#basic

# class animal:
#     def speak(self):
#         print('animal makes a sound')

# class dog(animal):
#     def bark(self):
#         print('dog barks')   

# d=dog()

# d.speak()
# d.bark()

    
#Constructor Inheritance with super()


# class person:
#     def __init__(self,name):
#         self.name=name

# class student(person):
#     def __init__(self,name,roll):
#         super().__init__(name)
#         self.roll=roll

#     def show(self):
#         print(f'name:{self.name},roll:{self.roll}')

# s=student('emil',101)

# s.show()


#Method Overriding

# class vehicle:
#     def start(self):
#         print('vehicle starting...')

# class car(vehicle):
#     def start(self):
#         super().start()
#         print('car starting...')
       
# c=car()
# c.start()
# # v=vehicle()
# # v.start()


#multilevel inheritance

# class grandparent:
#     def legacy(self):
#         print('grandparent legacy')

# class parent(grandparent):
#     def parent_method(self):
#         print('parent method')  

# class child(parent):
#     def child_method(self):
#         print('child method')

# c=child()
# c.legacy()
# c.parent_method()
# c.child_method()  

# Parent class
# class Animal:
#     def speak(self):
#         print("Animal speaks")

# # Child class
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")

# # Object create
# d = Dog()

# # Call parent method from child
# d.speak()   # Parent class method
# d.bark()    # Child class method