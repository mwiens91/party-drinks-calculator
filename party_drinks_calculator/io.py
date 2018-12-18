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
    while True:
        try:
            # Get input
            num_drinks = input("How many drinks do we need? ")

            # Validate
            num_drinks = int(num_drinks)

            # Good
            break
        except ValueError:
            print(Fore.RED + "Hey! Gimme integers!" + Style.RESET_ALL)

    print()  # padding

    while True:
        try:
            # Let the user know we need to add up to 100%
            print(
                "the following will ask for percentages of beer, wine, and hard liquor"
            )
            print(
                Fore.CYAN
                + "note that the percentages must add up to 100%"
                + Style.RESET_ALL
            )
            print()

            # Get input
            percent_beer = input("What percentage of beer do you want? [%] ")
            percent_wine = input("What percentage of wine do you want? [%] ")

            # Validate
            percent_beer = int(percent_beer)
            percent_wine = int(percent_wine)

            assert percent_beer + percent_wine <= 100

            # Good
            break
        except (AssertionError, ValueError):
            print(Fore.RED + "Oh no! Try again!" + Style.RESET_ALL)
            print()

    # Calculate percentage of hard liquor
    percent_hard_liquor = 100 - percent_beer - percent_wine

    print()
    print("Inferring %s%% of hard liquor" % percent_hard_liquor)

    return {
        "num_drinks": num_drinks,
        "percent_beer": percent_beer,
        "percent_wine": percent_wine,
        "percent_hard_liquor": percent_hard_liquor,
    }


def print_results(config_dict: dict, results_dict: dict):
    """Print calculation results to user.

    Args:
        config_dict: A dictionary containing config values.
        results_dict: A dictionary containing results.
    """
    # Build up a table
    unprocessed_rows = [
        ["beer", "required_beer", BEER_VERBOSE_NAME, "beer_cost"],
        ["wine", "required_wine", WINE_VERBOSE_NAME, "wine_cost"],
        [
            "hard liquor",
            "required_hard_liquor",
            HARD_LIQUOR_VERBOSE_NAME,
            "hard_liquor_cost",
        ],
    ]

    processed_rows = [
        [
            r[0],
            "%s of %s" % (results_dict[r[1]], r[2]),
            "%s%.2f" % (config_dict["currency_symbol"], results_dict[r[3]]),
        ]
        for r in unprocessed_rows
    ]

    # Format the total cost nicely
    total_cost = "%s%.2f" % (
        config_dict["currency_symbol"],
        results_dict["total_cost"],
    )

    # Build the final table
    results_table = [
        ["type", "quantity", "cost"],
        *processed_rows,
        ["total", "", total_cost],
    ]

    # Print the table
    print(tabulate(results_table, headers="firstrow", tablefmt="fancy_grid"))
