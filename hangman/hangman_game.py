from hangman_image import *
import random


def choose_word():
    word = open('word_list.txt', 'r').readlines()
    secret = random.choice(word).rstrip()
    secret_word = secret.upper()
    return secret_word


def hangman(word):
    guessed_letter = []
    turns = 0
    hidden_word = ['_'] * len(word)
    print(" ".join(hidden_word))
    while True:
        guess = input('Guess a letter... ').upper()
        if guess in word:
            if guess in guessed_letter:
                print('Already guessed, Try again!!')
            else:
                print('correct!')
                guessed_letter.append(guess)
                for i in range(len(word)):
                    if word[i] == guess:
                        hidden_word[i] = guess
                print('Current word: ', " ".join(hidden_word))
                if '_' not in hidden_word:
                    print(f"Game Over, You won.")
                    break

        else:
            turns += 1
            print('wrong try again')
            print(display_hangman(turns))
            if turns == 7:
                print(f'Game Over, You lost!\n The word was -> {word}')
                break


def play():
    user = input('What is your name? ')
    if input(f" Hi, {user}!! \n Ready to begin (Yes/No)... ").upper() == 'Y':
        word = choose_word()
        hangman(word)
    while True:
        if input('Play again (Yes/No)? ').upper() == 'Y':
            word = choose_word()
            hangman(word)
        else:
            exit()


if __name__ == '__main__':
    play()
