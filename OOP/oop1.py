# Position , name , age , Level , Salary
se1 = ["Software Engineer" , "Hossein", 27 , "Junior" , 500]
se2 = ["Software Engineer" , "Ali", 35 , "Senior" , 700]
d1 = ["Designer" , "Mohammad"]

#class
class SoftwareEngineer:

    # Class Attribute
    laghab = "Instructor"

    def __init__ (self, name, age, level, salary):
        #instance Attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    #Instance Method
    def code(self):
        print(f"{self.name} is writing Code")

    def code_in_language(self, language):
        print(f"{self.name} is writing Code in {language}...")

    #Dunder (Magic) Method
    def __str__(self):
        information = f"name = {self.name}, age = {self.age} , level = {self.level}"
        return information

    def __eq__ (self, other):
        return self.name == other.name and self.age == other.age

    @classmethod
    def entry_salary(age):
        if age < 25:
            return 500
        if age < 30:
            return 700
        return 900

#instance
se1 = SoftwareEngineer("Hossein" , 27, "Junior" , 500)
se2 = SoftwareEngineer("Ali" , 35, "Senior" , 700)
se3 = SoftwareEngineer("Ali" , 39, "Senior" , 700)


print(se1.entry_salary(24))
# print (se2 == se3)
# se1.code()
# se2.code()
# se1.code_in_language("Python")
# se2.code_in_language("C++")

# print(se1)
#instance
# se1 = SoftwareEngineer("Hossein" , 27, "Junior" , 500)
# print(se1.name , se1.age)
# print(SoftwareEngineer.laghab)

# se2 = SoftwareEngineer("Ali" , 35, "Senior" , 700)
# print(se2.laghab)

# Create Class (Blueprint)
# Create Instance (Object)

#instance method (self) => get arg and return value
#Special - Magic - Dunder Method => (__str__ , __eq__)
# @staticmethod , @ClassMethod