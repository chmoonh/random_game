import random

minimum=int(input('minimum: '))
maximum=int(input('maximum: '))

answer = random.randrange(minimum, maximum + 1)

def guess(guess):
    guess=int(input('guess number: '))
    if guess==answer:
        print('correct')
    else:
        if guess < answer:
            print('up')
        else:minimum=int(input('minimum: '))
            print('down')

while guess != answer:
    guess(guess)
