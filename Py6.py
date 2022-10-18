#1
def pattern(n):
    for i in n:
        print("/", end=" " )
        print("*" * int(i))
n = "35079"
pattern(n)

#2
import random
run = True
while run:
    user_input = int(input('Enter Number: '))
    if user_input == random.randrange(1,10):
        print('You won!')
        run = False
    else:
        print('try again!')
        continue

#3
def validate_password(password):
  special_chars =['$', '!', '@', '#', '%', '&']
  validated = True
  msg = ''

  if len(password) < 6:
    msg = 'Password length must be at least 6'
    validated = False
    
  elif len(password) > 16:
    msg = 'Password length must not be greater than 16'
    validated = False

  elif not any(char.isdigit() for char in password):
    msg = 'Password should have at least one number'
    validated = False

  elif not any(char.isupper() for char in password):
    msg = 'Password should have at least one uppercase letter'
    validated = False

  elif not any(char.islower() for char in password):
    msg = 'Password should have at least one lowercase letter'
    validated = False
        
  elif not any(char in special_chars for char in password):
    msg = 'Password should have at least one special character'
    validated = False

    return { 'is_valid': validated, 'message': msg }

print(validate_password('Hello1#'))