# Learning intentions:
# - Create a class pet with same information as in previous examples
# - Create an object instance of class pet

class Pet:
    def __init__(self, name, category, age):
        self.name = name
        self.category = category
        self.age = age
        self.vaccinated = False
        self.ccard = 'unknown'
        self.billing_address = 'unknown'
        self.owner_name = 'unknown'
        self.account_balance = 0

p1 = Pet('Bonnie', 'Cat', 3)
p2 = Pet('Foxy', 'Dog', 5)

print(p2.name)
print(p2.category)
print(p2.vaccinated)

p2.owner_name = 'John'

print(p2.owner_name)


#ACTIVITIES:
#1. Print out vaccination status of Bonnie
#2. Create another pet named Foxy who is a dog
#3. Add the following attributes to the pet class:
# - credit card
# - billing address
# - owner name (preset to unknown)
# - account balance (pre set to 0)