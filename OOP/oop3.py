# Getter & Setter

# _X is called “Protected” attribute
# __X is called “Private” attribute


class SoftwareEngineer:
    
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        self._salary = None
        self._num_bugs_solved = 0


    def code(self):
        self._num_bugs_solved += 1

    #Getter
    def get_salary(self):
       return self._salary
    #Setter
    def set_salary(self, base_value):
        self._salary = self._calculate_salary(base_value)
        #check Value , enforce constraints
        # if value < 1000:
        #     self._salary = 1000
        # if value > 20000:
        #     self._salary = 20000
        # self._salary = value

    def _calculate_salary (self, base_value):
        if self._num_bugs_solved < 10:
            return base_value
        if self._num_bugs_solved < 100:
            return base_value * 2
        return base_value * 3



se = SoftwareEngineer("Hossein" , 28)

for i in range(300):
    se.code()

print(se._num_bugs_solved)
se.set_salary(6000)
print(se.get_salary())