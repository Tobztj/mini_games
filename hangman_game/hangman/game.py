from hangman.emoji import emoji_converter
from hangman.image import display_hangman
import random

user = input('What is your name? ')


def choose_word(file):
    word = open(file, 'r').readlines()
    secret = random.choice(word).rstrip()
    secret_word = secret.upper()
    return secret_word


def hangman(word):
    guessed_letter = []
    turns = 7
    hidden_word = ['_'] * len(word)
    print(" ".join(hidden_word))
    while True:
        guess = input('Guess a letter... ').upper()
        if guess in word:
            if guess in guessed_letter:
                text = 'Already guessed, :| try again!'
                emoji_converter(text)
            else:
                text = f'Well done {user}, you guessed right :)'
                emoji_converter(text)
                guessed_letter.append(guess)
                for i in range(len(word)):
                    if word[i] == guess:
                        hidden_word[i] = guess
                print('Current word: ', " ".join(hidden_word))
                if '_' not in hidden_word:
                    text = f"Congratulations {user} you won :D "
                    emoji_converter(text)
                    break

        else:
            turns -= 1
            text = f"Wrong :; {user} have {turns} turns left!!"
            emoji_converter(text)
            print(display_hangman(turns))
            if turns == 0:
                text = f'Game Over {user}, you lost :( The word was -> {word}!!'
                emoji_converter(text)
                break
