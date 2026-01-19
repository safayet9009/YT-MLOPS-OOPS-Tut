#initialize a class

class employee:
    #special mehod/magic method/dunder method-constructor
    def __init__(self):
        self.id=123
        self.salary=500000
        self.designation='SWE'
    def travel(self,destination):
        print("Employee is traveling to", destination)

#create an obj/instance of the class
sam=employee()

print(sam.id)
print(sam.salary)
print(sam.designation)
sam.travel("New York")