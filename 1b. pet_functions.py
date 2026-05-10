name = 'Bonnie'
animal_category = 'Cat'
age = 3
vaccinated = True
ccard = '3423 2326 7543 1234'
billing_address = '17 Park Drive, The Shire 2695'
owner_name = 'Alex Ngyuen'
account_balance = 129.95

def help():
  print('Welcome to the Pet Data Management System')
  print("Every vet's best friend")



#ACTIVITIES:
#There are many ways to complete these. How will you go about the job?
#1. Verify this number 1234 4334 1001 0000

num = '1234 4334 1001 0000'
if verify_credit_card(num) == True:
  print('VALID')
else:
  print('INVALID')
  
#2. Ask the user for a credit card number and let them know if it is valid
#3. If the credit card is valid then reduce balance by $39
#4. Write and test a function to vaccinate Bonnie 
