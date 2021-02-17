import random
print()
print()
print()
print()

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
        else:
            print('down')

while guess != answer:
    guess(guess)
