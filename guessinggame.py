import random as rand


answer = rand.randint(1,100)
guess = int(input('Enter a number: '))
tries = 1
error = abs(guess - answer)
while guess != answer:
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS')
    elif tries == 1:
        if abs(guess - answer) <= 10:            
            print('WARM!')
        else:
            print('COLD!')
    elif error > abs(guess - answer):
        print('WARMER!')
    else:
        print('COLDER!')
    error = abs(guess - answer)
    tries += 1
    guess = int(input('Try again: '))

print("You've guessed correctly after ", tries, " tries!")    
