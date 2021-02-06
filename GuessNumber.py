import random

def guess(x):
    random_number = random.randint(1 , x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 to {x}: '))
        if guess < random_number:
            print('Sorry!, Guess Again. Too Low')
        elif guess > random_number:
            print('Sorry!, Guess Again. Too High')

    print (f'Yes! Your Guess is Correct! your number is {random_number}')

guess(20)