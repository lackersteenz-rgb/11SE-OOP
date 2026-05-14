# Learning intentions:
# - Create a method (function belonging to a class)
# - Discuss the use of attributes in the method

class Pet:
    def __init__(self, name, category, age = 0):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False
        self.account_balance = 0
    
    def have_birthday(self):
        self.age += 1

    def vaccinated(self):
        if self.vaccinated == True:
            print(self.name,'is already vaccinated')
        else:
            self.vaccinated = True
        
    def clear_balance(self):
        self.account_balance = 0

    def calculate_human_age(self):
        if self.category == 'Dog':
            print(self.name,'human age:',self.age*7)
        elif self.category == 'Cat':
            print(self.name,'human age:',self.age*6)
        else:
            print(self.name,'human age is unknown')

    def __str__(self):
        payment_status = 'unregistered'
        if len(self.ccard) == 19:
            payment_status = 'registered'
        
    my_status = 'Name: ' + self.name +'\nCategory: ' + self.category + '\nAge: ' + 
str(self.age) +'\nPayment status: ' + payment_status + '\nVaccinated: '+ 
str(self.vaccinated)
        return my_status
#It is correct, exactly. But still reports an error.

p1 = Pet(name = 'Bonnie', category = 'Cat', age = 10)
p1.have_birthday()
p1.vaccinate()
p1.vaccinate()

print(p1)
p1.calculate_human_age()
    

    
    

#ACTIVITIES:
#1. Add another method to vaccinate the pet
#2. Add another attribute for account balance then add a method to clear balance
#3. Add a method to print the animals age in human years use a multiplier of 7 if animal is a dog and a multiplier of 6 if it is a cat
# Use print statements to ensure you have comeplted each activity correctly.