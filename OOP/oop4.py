#Properties in Python

class SoftwareEngineer:
    
    def __init__ (self):
        self._salary = None

    @property
    def salary(self):
       return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value
    
    # @salary.deleter
    # def salary(self):
    #     del self._salary
    

se = SoftwareEngineer() # Instance Of Class!
se.salary = 500 # Set
print(se.salary) # Get
del se.salary
print(se.salary) # Get



#Encapsulation
#abstraction
# Public , Private, Protected
# X , __X , _X
# Getter / Setter
#Getter -> @Property
#Setter -> @X.setter