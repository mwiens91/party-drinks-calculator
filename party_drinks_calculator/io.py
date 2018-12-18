"""Contains functions for displaying and retreiving info."""

from colorama import Fore, Style
from tabulate import tabulate
from .constants import (
    BEER_VERBOSE_NAME,
    WINE_VERBOSE_NAME,
    HARD_LIQUOR_VERBOSE_NAME,
)
from .version import VERSION


def print_welcome_message(config_dict: dict):
    """Print a welcome message.

    Args:
        config_dict: A dictionary with values from the user's config
            file.
    """
    # Welcome the user
    welcome_string = "party drinks calculator v" + VERSION

    print(Style.BRIGHT + welcome_string + Style.RESET_ALL)
    print("-" * len(welcome_string))
    print()

    # Let them know what prices we're using
    print("using average prices in %s" % config_dict["currency_name"])
    print()

    table = [
        [BEER_VERBOSE_NAME, config_dict["price_per_beer"]],
        [WINE_VERBOSE_NAME, config_dict["price_per_wine"]],
        [HARD_LIQUOR_VERBOSE_NAME, config_dict["price_per_hard_liquor"]],
    ]

    # Add currency symbol to the table values
    for row in table:
        row[1] = config_dict["currency_symbol"] + row[1]

    # Print a table of the prices
    print(tabulate(table, tablefmt="plain"))


def get_users_values() -> dict:
    """Gets required values from the user.

    Returns:
        A dictionary containing parsed values inputted by the user.
    """
    # TODO code me
    pass
