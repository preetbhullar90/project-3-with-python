"""
import colorama, os,random,google-auth and gspread link with run.py.
"""
import os
import random
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
    print(Fore.YELLOW + Style.BRIGHT + "wait...")
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