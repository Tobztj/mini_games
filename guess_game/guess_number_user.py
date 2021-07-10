import random


def computer_guess(x):
    feedback = ""
    low = 1
    high = x
    while feedback != 'c'and low != high:
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high (H), too low (L), correct (C)? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1



computer_guess(20)