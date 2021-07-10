import random

# x = random.randint(1, 100)
# print(x)
#
# b = random.choice([x])
# count = 0
# while count <= 3:
#     a = input('Guess a number.. ')
#
#
#     if a == b:
#         print('Correct')
#     else:
#         print("Try again")
#         count += 1
#
#     if count == 3:
#         print(f"failed, the correct number -> {b}")
#         exit()

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess > random_number:
            print('Too high!')
        elif guess < random_number:
            print('Too Low')
    print(f'Correct -> {random_number}')



x = random.randint(5, 1000)
guess(x)