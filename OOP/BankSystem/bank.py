# Parent Class : User
# + Hold details from User
# + function to show user details

# Child Class : Bank
# + Store details about account balance
# + Store details about account amount
# + 3 functions : deposit - withdraw - view_balance

#Parent Class
class User():
    def __init__(self,name,age,gender) :
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self) :
        print("Personal Details")
        print("")
        print("Name ", self.name)
        print("Age ", self.age)
        print("Gender ", self.gender)

#Child Class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name,age,gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + amount
        print("Account balance has been Updated :" , self.balance)
    
    def withdraw (self , amount):
        self.amount = amount
        if(self.amount > self.balance):
            print("Insufficent Fund | Balance Availble :" , self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been Updated :" , self.balance)

    def view_balance (self):
        self.show_details()
        print ("Account Balance: " , self.balance)

    
