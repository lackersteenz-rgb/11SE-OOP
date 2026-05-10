name = 'Bonnie'
animal_category = 'Cat'
age = 3
vaccinated = True
ccard = '3423 2326 7543 1234'
billing_address = '17 Park Drive, The Shire 3695'
owner_name = 'Alex Ngyuen'
account_balance = 129.95

# ACTIVITIES:
#Theere are many ways to complete these tasks. How will you do them?

#1 Increase age by 1 year
age = age + 1
print(age)

#2 Change the address to 17 Park Street
billing_address = '17 Park Street, The Shire 3695'
print(billing_address)

#3 No longer vaccinated (change state of vaccinated)
vaccinated = 'False'
print(vaccinated)

#4 Prompt user for updated credit card number and save new number
ccard = input('Enter credit card: ')
print(ccard)

#5 Change owner name to Alex Jones
owner_name = 'Alex Jones'
print(owner_name)

#6 Subtract $25 from account balance
account_balance -=25
print(account_balance)

#7 Print all variables in a list format
print(name, animal_category, age, vaccinated, ccard, billing_address, owner_name, account_balance)