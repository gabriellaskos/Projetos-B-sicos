import random

secret_number = random.randint(0,20)

# loop start
gotRight = False

attempts = 0

while not gotRight:
    attempt = int(input('Write your try --> '))
    attempts += 1
    
    if attempt < secret_number:
        print(f'too low :(  the number was --> {secret_number}')
        secret_number = random.randint(0,20)
        
        
    elif attempt > secret_number:
        print(f'too high :( the number was --> {secret_number}')
        secret_number = random.randint(0,20)
         
        
    else:
        print(f'goated! You got it right in --> {attempts} !')
        gotRight = True
    