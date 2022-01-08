"""
import colorama, os,random,google-auth and gspread link with run.py.
"""
import random
import time
import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, Style
from classes.ascii_art import hangman_ascii_text
from classes.ascii_art import user_no_ready
from classes.ascii_art import after_finish_game
from classes.display_image import display_hangman
from classes.ascii_art import welcome_hangman
from classes.terminal_clear import ClearDisplay

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("hangman_game")


class Start(ClearDisplay):
    """
    Creates object and play the game by
    calling object of the other classes
    """

    def __init__(self):
        self.welcome_game()

    def get_all_words(self):
        """
        This function is for to
        get all the words from the gspread sheet.
        """
        lists = SHEET.worksheet("words_List").get_all_values()
        for item in lists:
            word_list = item
            return word_list

    def welcome_game(self):
        """
        Get name input from the users.
        while loop runs until the user does not provide a valid input.
        If the input is valid the user will see a welcome message with
        the username and hangman text.
        """
        welcome_hangman()
        print("\n")
        time.sleep(.5)
        global NAME
        NAME = input(Fore.YELLOW + Style.BRIGHT + "Please enter your name: ")
        print("\n")
        print("wait...")
        time.sleep(2)
        self.clear_terminal()
        print("\n")
        while not NAME.isalpha() and NAME.isnumeric() or len(NAME) < 2:
            print("\n")
            print("wait...")
            time.sleep(2)
            self.clear_terminal()
            print(
                Fore.RED + "Sorry, Your name is invalid, please "
                "enter your full name in letters\n"
            )
            print("\n")
            NAME = input(Fore.YELLOW + Style.BRIGHT +
                         "Please enter your name: ")
        else:
            print("\n")
            print("Game loading...")
            print("\n")
            time.sleep(2)
            self.clear_terminal()
            print("\033[1;34m")
            hangman_ascii_text()
            time.sleep(0.5)
            self.random_word()

    def game_instruction(self):
        """
        while loop  will continue to run until the user
        selects the N or Y option.
        if the user selects Y then the game will start
        and if the N option is selected the game will end.
        """
        print(Fore.YELLOW + Style.BRIGHT + "wait...")
        time.sleep(0.5)
        self.clear_terminal()
        print(Fore.BLUE + Style.BRIGHT + "\n\033[1;34mHow to play:\n ")
        time.sleep(0.5)
        print("\n1. The theme of the game is fruits.")
        time.sleep(0.5)
        print("\n2. You need to guess the word correctly from the word list.")
        time.sleep(0.5)
        print("\n3. You need to write a letter "
              "of your choice and press enter.")
        time.sleep(0.5)
        print("\n4. If your guess is correct then the "
              "letter will show within \n\n   the dashes in the row.")
        time.sleep(0.5)
        print("\n5. If your guess is "
              "wrong, then you will lose 1 life out of 7 \n\n   and"
              " you will get a image of a hangman.")
        time.sleep(0.5)
        print("\n6. You can play until you run out of"
              " lives or you guess all the letters.\n")
        time.sleep(0.5)
        print(
            Fore.YELLOW + Style.BRIGHT + NAME.capitalize() +
            " are you ready to play?\n")
        time.sleep(0.5)
        ready = input(
            "Please press Y for" " YES or press N for NO : "
            ).upper()
        while ready != "Y" and ready != "N":
            self.clear_terminal()
            ready = input(
                NAME.capitalize() +
                " Please press Y for YES or press N for NO: "
            ).upper()
        if ready == "Y":
            time.sleep(0.5)
            self.clear_terminal()
            word = random.choice(self.get_all_words())
            self.play_game(word)
        else:
            self.clear_terminal()
            print(Fore.BLUE + Style.BRIGHT + "\n")
            self.random_word()

    def playgame_again(self):
        """
        This function is for playing again.
        while loop runs until the user has  not selected Y or N.
        If user selects Y game will run again, but if user selects N the
        game will exit with their username and a nice message.
        """
        play_again = input(' '*10 +
                           Fore.YELLOW + Style.BRIGHT +
                           "Would you like to play "
                           "again? If Yes press Y If No press N: "
                           ).upper()
        while play_again != "Y" and play_again != "N":
            self.clear_terminal()
            play_again = input(
                ' '*10 + "Would you like to play again? "
                "If Yes press Y If No press N: "
            ).upper()
        if play_again == "Y":
            time.sleep(0.5)
            self.clear_terminal()
            word = random.choice(self.get_all_words())
            self.play_game(word)
        else:
            self.clear_terminal()
            print(
                Style.BRIGHT + Fore.BLUE + "Thank you,", NAME.capitalize(),
                "for playing, see you again",
            )
            print("\n")
            after_finish_game()

    def random_word(self):
        """
        In this function while loop runs until
        the user does not select the Y or I
        option.This function runs after when the user enters their name.
        If the user selects I they will get instructions or If the user selects
        Y then, they will go straight to the game.
        """
        print(f"{' Main Menu ' :-^80}")
        print('\n\n')
        print(f"{' Y: Play  ':^80}")
        print('\n')
        print(f"{' I: Instruction ':^80}")
        print('\n')
        print(f"{' Q: Quit ':^80}")
        print('\n')
        get_ready = input(
            Fore.YELLOW + Style.BRIGHT + NAME.capitalize() + ","
            " Please choose your choice (Y, I, Q): ").upper()
        while get_ready != "Y" and get_ready != "I" and get_ready != "Q":
            self.clear_terminal()
            print(Style.BRIGHT + Fore.BLUE)
            hangman_ascii_text()
            print(f"{' Main Menu ' :-^80}")
            print('\n\n')
            print(f"{' Y: Play  ':^80}")
            print('\n')
            print(f"{' I: Instruction ':^80}")
            print('\n')
            print(f"{' Q: Quit ':^80}")
            print('\n')
            get_ready = input(
                Fore.YELLOW + Style.BRIGHT + NAME.capitalize() + ","
                " Please choose your choice (Y, I, Q): ").upper()
        if get_ready == "Y":
            self.clear_terminal()
            word = random.choice(self.get_all_words())
            self.play_game(word)
        elif get_ready == "I":
            self.clear_terminal()
            self.game_instruction()
        elif get_ready == "Q":
            self.clear_terminal()
            print(
                Style.BRIGHT + Fore.BLUE + "Thank you,", NAME.capitalize(),
                "for trying see you again when you are ready",
            )
            print("\n")
            user_no_ready()
        else:
            self.clear_terminal()
            self.random_word()

    def play_game(self, words):
        """
        In this function I used loops and many
        if else statments to get the words.
        While loop runs until the user does not use
        all the tries available.
        6 chances are availble before the game will end.
        this function prompts the user to enter a letter
        if an incorrect letter or
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
        self.clear_terminal()
        print(Fore.BLUE + Style.BRIGHT + display_hangman(user_tries))
        print(Style.BRIGHT + words_complete.center(80))
        time.sleep(0.5)
        print("\n")
        while not word_guess and user_tries > 0:
            letter_guess = input(Fore.YELLOW + Style.BRIGHT +
                                 ' '*28 + "Guess a letter or word: ").upper()
            self.clear_terminal()
            letter.append(letter_guess)
            no_repeat_letter = list(dict.fromkeys(letter))
            string_one = (
                  Fore.BLUE + Style.BRIGHT +
                  "You used these letters: " + ", ".join(no_repeat_letter))
            print(string_one.center(95))
            if len(letter_guess) == 1 and letter_guess.isalpha():
                if letter_guess in word_guess_letter:
                    print(' '*25 +
                          Fore.RED + Style.BRIGHT +
                          "you have already selected the letter " +
                          letter_guess.upper() + "!" + Fore.BLUE
                          )
                elif letter_guess not in words:
                    print(' '*27 +
                          Fore.RED + Style.BRIGHT +
                          letter_guess.upper(),
                          " is not a part of the word :(",
                          Fore.BLUE,)
                    print('\n')
                    print(' '*30 +
                          "You have", user_tries - 1, "tries left")
                    user_tries -= 1
                    word_guess_letter.append(letter_guess)
                else:
                    print(' '*25 + Fore.GREEN + Style.BRIGHT +
                          "You are doing well,", letter_guess.upper(),
                          " is in the word!" + Fore.BLUE)
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
                    print(' '*100 +
                          Fore.RED + Style.BRIGHT + " has already been tried",
                          letter_guess.upper() + "!",
                          Fore.BLUE,)
                elif letter_guess != words:
                    print(' '*100 + letter_guess.upper(),
                          "is not a part of the word :(", Fore.BLUE,)
                    user_tries -= 1
                    word_guess_words.append(letter_guess)
                else:
                    word_guess = True
                    words_complete = words
            else:
                print(' '*30 + Fore.RED + Style.BRIGHT +
                      "This is an invalid input", Fore.BLUE)
            print(Fore.BLUE + Style.BRIGHT + display_hangman(user_tries))
            print(words_complete.center(80))
            print('\n')
        if word_guess:
            print(' '*10 +
                  Fore.GREEN + Style.BRIGHT + "Congratulations!,",
                  NAME.capitalize() +
                  "you guessed the word correctly!",
                  Fore.BLUE,)
        else:
            print(' '*5 +
                  Fore.BLUE + Style.BRIGHT + "Sorry,",
                  NAME.capitalize(),
                  " you ran out of tries.The correct word was ",
                  Fore.RED + Style.BRIGHT + words + Fore.BLUE + Style.BRIGHT,
                  ". Better luck next time !",)
        self.playgame_again()


Start()
