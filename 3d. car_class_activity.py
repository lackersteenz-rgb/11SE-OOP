# Learning intentions:
# - Create a car class example
# - Use attributes: make, model, year and price
# - Create a __str__ method that prints make and model

class Car:
    def __init__(self,make,model,year,price=None):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.for_sale = False

    def __str__(self):
        if self.for_sale == True:
            return '|Make: '+self.make+' | Model: '+self.model +'| FOR SALE |'
        else:
            return '|Make: '+self.make+' | Model '+self.model +'| NOT FOR SALE |'

c1 = Car('Mazda','6',2005)
c2 = Car('Tesla','S',2017)
c2.for_sale = True
c3 = Car('Porche','911',2020)
c4 = Car('Golf','TDI',2016)

cars = [c1,c2,c3,c4]

for car in cars:
    print(car)


#ACTIVITIES:
#1. Istantiate another car object
#2. Add another attribute (for_sale)
#3. Add sale status for sale or not for sale to the __str__ method
#4. Create 2 more cars and print all car statuses with a loop