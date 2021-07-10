from hangman_image import *
from emoji import *
import random

user = input('What is your name? ')


def choose_word():
    word = open('word_list.txt', 'r').readlines()
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


def play():
    text = f" Hi, {user} :w"
    emoji_converter(text)
    text = input("Ready to begin (Yes/No)... ").upper()
    if text == 'Y':
        word = choose_word()
        hangman(word)
    elif text == 'N':
        text = "Bye :w :("
        emoji_converter(text)
        exit()

    while True:
        text = input('Play again (Yes/No)? ').upper()
        count = 1
        if text == 'Y':
            count += 1
            emoji_converter(message=f"Round {count} :D")
            word = choose_word()
            hangman(word)
        else:
            emoji_converter(message="Bye :w see you soon :(")
            exit()


if __name__ == '__main__':
    play()
