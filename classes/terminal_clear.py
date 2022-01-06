"""
Create class to clear the terimal
"""
import os


class ClearDisplay():
    """
    Create a static function to be used for multiple classes
    """

    def clear_terminal(self):
        """"
        Clears the console
        """
        os.system('cls' if os.name == 'nt' else 'clear')
