#Tutorial 3 Lists:
#1. Create an example of parallel lists eg: pet_name, species, age, vaccination_status for three pets
#2. Use a for loop to print parallel list details. This will mean that one complete printout will look like:
'''
Pet name: Foxy
Species: Dog
Age: 8
Vaccination Status: False
'''
#3. Demonstrate what happens when an item is deleted

names = ['Foxy', 'Bella', 'Hootie']
animal_categories = ['Dog', 'Rabbit', 'Blowfish']
ages = [8,3,34]
vaccinated = [False, False, True]

for i in range(len(names)):
    print('Pet name:', names[i])
    print('Category:', animal_categories[i])
    print('Age:', ages[i])
    print('Vaccinated',vaccinated[i])
    print('')
    


  #ACTIVITIES:
# In each activity test out that the printing of data is still valid

#1. Add a new animal named Hootie, its a blowfish, it is 34 years
#2. Vaccinate an unvaccinated animal (create vaccination)
#3. Remove an animal and make sure that all the printing is correct