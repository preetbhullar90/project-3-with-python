"""
import time,os and colorama
"""
import os
import time
from colorama import Fore, Style


def hangman_ascii_text():
    """
    This function used for show ASCII hangman in game mainu
    This function run after when user enter the name
    """
    print(
            """
        ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
        ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
        ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
        ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
        ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
        ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
            """)


def user_no_ready():
    """
    This function create if user not ready to play
    """
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


def after_finish_game():
    """
    This function run if users finished the game but they don,t
    want to play again
    """
    print(
                """
 dP""b8  dP"Yb   dP"Yb  8888b.      88""Yb Yb  dP 888888
dP   `" dP   Yb dP   Yb  8I  Yb     88__dP  YbdP  88__
Yb  "88 Yb   dP Yb   dP  8I  dY     88""Yb   8P   88""
 YboodP  YbodP   YbodP  8888Y"      88oodP  dP    888888

            """
        )


def welcome_hangman():
    """
    This function show welcome to hangman message
    """
    os.system("cls" if os.name == "nt" else "clear")
    time.sleep(.7)
    print(Fore.BLUE + Style.BRIGHT + '\n' * 4)
    print("*" * 80)
    print("""
        db   d8b   db d88888b db       .o88b.  .d88b.  .88b  d88. d88888b
        88   I8I   88 88'     88      d8P  Y8 .8P  Y8. 88'YbdP`88 88'
        88   I8I   88 88ooooo 88      8P      88    88 88  88  88 88ooooo
        Y8   I8I   88 88~~~~~ 88      8b      88    88 88  88  88 88~~~~~
        `8b d8'8b d8' 88.     88booo. Y8b  d8 `8b  d8' 88  88  88 88.
         `8b8' `8d8'  Y88888P Y88888P  `Y88P'  `Y88P'  YP  YP  YP Y88888P
    """)
    print("*" * 80)
    time.sleep(.6)

    os.system("cls" if os.name == "nt" else "clear")
    print('\n' * 4)
    print("*" * 80)
    print("""
                           d888888b  .d88b.
                           `~~88~~' .8P  Y8.
                              88    88    88
                              88    88    88
                              88    `8b  d8'
                              YP     `Y88P'
    """)
    print("*" * 80)
    time.sleep(.6)

    os.system("cls" if os.name == "nt" else "clear")
    print('\n' * 4)
    print("*" * 80)
    print("""
            db   db  .d8b.  d8b   db  d888b  .88b  d88.  .d8b.  d8b   db
            88   88 d8' `8b 888o  88 88' Y8b 88'YbdP`88 d8' `8b 888o  88
            88ooo88 88ooo88 88V8o 88 88      88  88  88 88ooo88 88V8o 88
            88~~~88 88~~~88 88 V8o88 88  ooo 88  88  88 88~~~88 88 V8o88
            88   88 88   88 88  V888 88. ~8~ 88  88  88 88   88 88  V888
            YP   YP YP   YP VP   V8P  Y888P  YP  YP  YP YP   YP VP   V8P
    """)
    print("*" * 80)
    time.sleep(.6)
