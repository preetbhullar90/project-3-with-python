"""
import colorama, os,random,google-auth and gspread link with run.py.
"""
import os
import random
import time
import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, Style

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("hangman_game")


def get_all_words():
    """
    This function is for to
    get all the words from the gspread sheet.
    """
    lists = SHEET.worksheet("words_List").get_all_values()
    for item in lists:
        word_list = item
        return word_list


def welcome_game():
    """
    Get name input from the users.
    while loop runs until the user does not provide a valid input.
    If the input is valid the user will see a welcome message with
    the username and hangman text.
    """
    print("\n")
    global NAME
    NAME = input(Fore.YELLOW + Style.BRIGHT + "Please enter your name: ")
    print("\n")
    time.sleep(2)
    os.system("cls" if os.name == "nt" else "clear")
    print("\n")
    while not NAME.isalpha() or len(NAME) < 2:
        print("\n")
        print(Fore.YELLOW + Style.BRIGHT + "wait...")
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
        print(
            Fore.RED + "Sorry, Your name is invalid, please "
            "enter your full name in letters\n"
        )
        print("\n")
        NAME = input(Fore.YELLOW + Style.BRIGHT + "Please enter your name: ")
    else:
        print("\n")
        print(Fore.YELLOW + Style.BRIGHT + "Game loading...")
        print("\n")
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
        print("\033[1;34m")
        print(
            """
        ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
        ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
        ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
        ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
        ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
        ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
        """
        )
        print("\n\n")
        print(
            Fore.BLUE + Style.BRIGHT + "Hello, " + NAME.capitalize(),
            "Welcome to hangman!",
        )
        time.sleep(0.5)
        random_word()


def game_instruction():
    """
    while loop  will continue to run until the user selects the N or Y option.
    if the user selects Y then the game will start
    and if the N option is selected the game will end.
    """
    print(Fore.YELLOW + Style.BRIGHT + "wait...")
    time.sleep(0.5)
    os.system("cls" if os.name == "nt" else "clear")
    print(
        Fore.BLUE + Style.BRIGHT + "\033[1;34mHow to play:\n\n1. "
        "You need to guess the word correctly from the word list."
        "\n2. You need to write a letter "
        "of your choice and press enter.\n3. If your guess is correct,"
        "then the "
        "letter will show within the dashes in the row.\n4. If your guess is "
        "wrong, then you will lose 1 life out of 7 and"
        " you will get a image of a hangman.\n5. You "
        "can play until you run out of"
        " lives or you guess all the letters.\n"
    )
    print(
        Fore.YELLOW + Style.BRIGHT + NAME.capitalize() +
        " are you ready to play?")
    ready = input(
        Fore.YELLOW + Style.BRIGHT +
        "Please press Y for" " YES or press N for NO : "
    ).upper()
    while ready != "Y" and ready != "N":
        os.system("cls" if os.name == "nt" else "clear")
        ready = input(
            Fore.YELLOW + Style.BRIGHT + NAME.capitalize() +
            " Please press Y for"
            "YES or press N for NO: "
        ).upper()
    if ready == "Y":
        time.sleep(0.5)
        os.system("cls" if os.name == "nt" else "clear")
        word = random.choice(get_all_words())
        play_game(word)
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print(
            Style.BRIGHT + Fore.BLUE + "Thank you,",
            NAME.capitalize(),
            "for trying see you again when you are ready",
        )
        print("\n")
        print(
            """
        O)) O))   O))      O))O))))))))
        O)    O))  O))    O)) O))
        O)     O))  O)) O))   O))
        O))) O)       O))     O))))))
        O)     O))    O))     O))
        O)      O)    O))     O))
        O)))) O))     O))     O))))))))

                """
        )


def playgame_again():
    """
    This function is for playing again.
    while loop runs until the user has  not selected Y or N.
    If user selects Y game will run again, but if user selects N the
    game will exit with their username and a nice message.
    """
    play_again = input(
        Fore.YELLOW + Style.BRIGHT + "Would you like to play "
        "again? If Yes press Y If No press N: "
    ).upper()
    while play_again != "Y" and play_again != "N":
        os.system("cls" if os.name == "nt" else "clear")
        play_again = input(
            Fore.YELLOW + Style.BRIGHT + "Would you like to play again? "
            "If Yes press Y If No press N: "
        ).upper()
    if play_again == "Y":
        time.sleep(0.5)
        os.system("cls" if os.name == "nt" else "clear")
        word = random.choice(get_all_words())
        play_game(word)
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print(
            Style.BRIGHT + Fore.BLUE + "Thank you,",
            NAME.capitalize(),
            "for playing, see you again",
        )
        print("\n")
        print(
            """
 dP""b8  dP"Yb   dP"Yb  8888b.      88""Yb Yb  dP 888888
dP   `" dP   Yb dP   Yb  8I  Yb     88__dP  YbdP  88__
Yb  "88 Yb   dP Yb   dP  8I  dY     88""Yb   8P   88""
 YboodP  YbodP   YbodP  8888Y"      88oodP  dP    888888

"""
        )


def random_word():
    """
    In this function while loop runs until the user does not select the Y or I
    option.This function runs after when the user enters their name.
    If the user selects I they will get instructions or If the user selects
    Y then, they will go straight to the game.
    """
    print("\n")
    get_ready = input(
        Fore.YELLOW + Style.BRIGHT + NAME.capitalize() +
        " Please press Y to play"
        " and press I for instructions: "
    ).upper()
    while get_ready != "Y" and get_ready != "I":
        os.system("cls" if os.name == "nt" else "clear")
        get_ready = input(
            Fore.YELLOW + Style.BRIGHT + NAME.capitalize() + ","
            "are you ready to play"
            "if YES press Y if NO press N: "
        ).upper()
    if get_ready == "Y":
        print("\n")
        print(Fore.YELLOW + Style.BRIGHT, "Game loading...")
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
        word = random.choice(get_all_words())
        play_game(word)
    else:
        os.system("cls" if os.name == "nt" else "clear")
        game_instruction()


def play_game(words):
    """
    In this function I used loops and many if else statments to get the words.
    While loop runs until the user does not use all the tries available.
    6 chances are availble before the game will end.
    this function prompts the user to enter a letter if an incorrect letter or
    invalid charecter is entered  the user will recive
    a message according to their input.
    """
    words_complete = "-" * len(words)
    time.sleep(0.5)
    word_guess = False
    word_guess_letter = []
    word_guess_words = []
    user_tries = 6
    letter = []

    print(Fore.YELLOW + Style.BRIGHT + "wait...")
    time.sleep(0.5)
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.BLUE + Style.BRIGHT + display_hangman(user_tries))
    print(Style.BRIGHT + words_complete)
    time.sleep(0.5)
    print("\n")
    while not word_guess and user_tries > 0:
        letter_guess = input(
            Fore.YELLOW + Style.BRIGHT + "Guess a letter or word: "
        ).upper()
        os.system("cls" if os.name == "nt" else "clear")
        letter.append(letter_guess)
        print(
            Fore.BLUE + Style.BRIGHT +
            "You used these letters: " + ", ".join(letter))
        print("\n")
        if len(letter_guess) == 1 and letter_guess.isalpha():
            if letter_guess in word_guess_letter:
                print(
                    Fore.RED +
                    Style.BRIGHT +
                    "you have already selected the letter " +
                    letter_guess.upper() +
                    "!" + Fore.BLUE
                )
            elif letter_guess not in words:
                print(
                    Fore.RED + Style.BRIGHT + letter_guess.upper(),
                    " is not a part of the word :(",
                    Fore.BLUE,
                )
                print("\n")
                print(
                    NAME.capitalize(),
                    "You have", user_tries - 1, "tries left")
                user_tries -= 1
                word_guess_letter.append(letter_guess)
            else:
                print(
                    Fore.GREEN + Style.BRIGHT + NAME.capitalize(),
                    "you are doing well,",
                    letter_guess.upper(),
                    "is in the word!" + Fore.BLUE,
                )
                word_guess_letter.append(letter_guess)
                word_as_list = list(words_complete)
                indices = [
                    i for i, letters in enumerate(words)
                    if letters == letter_guess
                ]
                for index in indices:
                    word_as_list[index] = letter_guess
                words_complete = "".join(word_as_list)
                if "-" not in words_complete:
                    word_guess = True
        elif len(letter_guess) == len(words) and letter_guess.isalpha():
            if letter_guess in word_guess_words:
                print(
                    Fore.RED + Style.BRIGHT + " has already been tried",
                    letter_guess.upper() + "!",
                    Fore.BLUE,
                )
            elif letter_guess != words:
                print(
                    Fore.RED + Style.BRIGHT + letter_guess.upper(),
                    "is not a part of the word :(",
                    Fore.BLUE,
                )
                user_tries -= 1
                word_guess_words.append(letter_guess)
            else:
                word_guess = True
                words_complete = words
        else:
            print(Fore.RED + Style.BRIGHT + "This is an invalid input",
                  Fore.BLUE)
        print(Fore.BLUE + Style.BRIGHT + display_hangman(user_tries))
        print(Fore.BLUE + Style.BRIGHT + words_complete)
        print("\n")
    if word_guess:
        print(
            Fore.GREEN + Style.BRIGHT + "Congratulations!,",
            NAME.capitalize(),
            "you guessed the word correctly!",
            Fore.BLUE,
        )
        print("\n")
    else:
        print(
            Fore.BLUE + Style.BRIGHT + "Sorry,",
            NAME.capitalize(),
            " you ran out of tries.The correct word was ",
            Fore.RED + Style.BRIGHT + words + Fore.BLUE + Style.BRIGHT,
            ". Better luck next time !",
        )
        print("\n")
    playgame_again()


def display_hangman(user_tries):
    """
    This function shows the image in the game according to the users input.
    If user selects the wrong answer then
    they will get the next image out of the 6 progressions of the hangman.
    This function runs until the user runs out of all their tries.
    """
    image_stages = [
        """

        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     / \\
        -
        """,
        """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     /
        -
        """,
        """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |
        -
        """,
        """
        --------
        |      |
        |      O
        |     \\|
        |      |
        |
        -
        """,
        """
        --------
        |      |
        |      O
        |      |
        |      |
        |
        -
        """,
        """
        --------
        |      |
        |      O
        |
        |
        |
        -
        """,
        """

        --------
        |      |
        |
        |
        |
        |
        -

        """,
    ]
    return image_stages[user_tries]


welcome_game()
