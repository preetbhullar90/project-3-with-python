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
        terminal = 'clear'
        if os.name in ('nt', 'dos'):
            terminal = 'cls'
        os.system(terminal)
