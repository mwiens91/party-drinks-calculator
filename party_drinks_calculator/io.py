"""Contains functions for displaying and retreiving info."""

from colorama import Fore, Style
from .version import VERSION


def print_welcome_message():
    """Print a welcome message."""
    welcome_string = "party drinks calculator v" + VERSION

    print(Style.BRIGHT + welcome_string + Style.RESET_ALL)
    print("-" * len(welcome_string))


def get_users_values() -> dict:
    """Gets required values from the user.

    Returns:
        A dictionary containing parsed values inputted by the user.
    """
    # TODO code me
    pass
