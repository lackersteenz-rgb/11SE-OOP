class Pet:
    def __init__(self, name, category, breed = None, age = 0):
        self._name = name
        self.__category = category
        self.__breed = breed
        self.age = age
        self.__ccard = 'unknown'
        self.vaccinated = False
        self.weight = 0

    def set_name(self,new_name):
        if type(new_name) == str:
            self._name = new_name
        else:
            print('Please use a string as a name attribute')

    def get_name(self):
        return self._name
    
    def get_weight(self, new_weight):
        if type(new_weight) == int or type(new_weight) == float:
            if new_weight > 0:
                self.weight = new_weight
            else:
                print('Please enter a positive number for weight')
        else:
            print('Please enter a number for weight')

    def have_birthday(self):
        self.age += 1

    def __str__(self):
        payment_status = 'unregistered'
        if len(self.__ccard) == 19:
            payment_status = 'registered'

        my_status = 'Name: ' + self._name +'\nCategory: ' + self.__category + '\nAge: ' + str(self.age) +'\nPayment status: ' + payment_status + '\nVaccinated: '+ str(self.vaccinated)
        return my_status

p1 = Pet(name = 'Bonnie', category = 'Cat', age = 10)

p1.set_weight(12)

print('Bonnies weight: ',p1.weight)
p1.set_name(56789876)
print(p1.get_name())
print(p1)  

   

#ACTIVITIES:
#1. Add attribute weight and write a getter method for weight
#2. Add setter method or weight and make sure it is a positive number (integer or float)