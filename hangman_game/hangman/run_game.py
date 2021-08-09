from hangman.game import *
from hangman.file_path import words as file


def play():
    text = f" Hi, {user} :w"
    emoji_converter(text)
    text = input("Ready to begin (Yes/No)... ").upper()
    if text == 'Y':
        word = choose_word(file)
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
