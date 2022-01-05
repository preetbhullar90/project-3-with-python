"""
funtion for display iamges
"""


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
