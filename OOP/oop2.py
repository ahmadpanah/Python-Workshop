# inherites, extend, override

class Employee:
    
    def __init__ (self, name, age , salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working...")


class SoftwareEngineer(Employee):
    
    def __init__ (self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    def work(self):
        print(f"{self.name} is coding...")

    def debug(self):
        print(f"{self.name} is debugging...")


class Designer(Employee):

    def work(self):
        print(f"{self.name} is designing...")

    def draw (self):
        print(f"{self.name} is drawing...")

se = SoftwareEngineer("Hossein" , 28, 8000, "Senior")

d = Designer("Ali" , 34 , 5000)


# Polymorphism

employees = [SoftwareEngineer("Mohammad", 25, 500 , "Senior"),
             SoftwareEngineer("Reza", 39, 900 , "Junior"),
             Designer("Farid" , 27 , 700)]


def motivate(employees):
    for employee in employees:
        employee.work()


motivate(employees)

#inhertance : ChildClass(BaseClass)
#inherit , extend , override
# super().__init__
#polymorphism