"""Calculate quantities."""

from math import ceil, floor
from .constants import (
    DRINKS_PER_BEER,
    DRINKS_PER_WINE,
    DRINKS_PER_HARD_LIQUOR,
    CEILING,
    FLOOR,
)


def calculate_liquor_quantities(
    config_dict: dict, user_dict: dict, rounding_method: str = CEILING
) -> dict:
    """Get liquor quantities and prices given our input.

    Args:
        config_dict: A dictionary containing config values.
        user_dict: A dictionary containing values inputted by the user.
        rounding_method (optional): The method to use for rounding.
            Must be one of the rounding constants found in the constants
            module.

    Returns:
        A dictionary containing calculated data.
    """
    # Calculate total required drinks
    total_required_drinks = user_dict["num_drinks"]

    required_beer_drinks = (
        total_required_drinks * user_dict["percent_beer"] / 100
    )
    required_wine_drinks = (
        total_required_drinks * user_dict["percent_wine"] / 100
    )
    required_hard_liquor_drinks = (
        total_required_drinks * user_dict["percent_hard_liquor"] / 100
    )

    if rounding_method == CEILING:
        round_fn = ceil
    elif rounding_method == FLOOR:
        round_fn = floor
    else:
        round_fn = round

    required_beer = round_fn(required_beer_drinks / DRINKS_PER_BEER)
    required_wine = round_fn(required_wine_drinks / DRINKS_PER_WINE)
    required_hard_liquor = round_fn(
        required_hard_liquor_drinks / DRINKS_PER_HARD_LIQUOR
    )

    # Calculate prices
    price_per_beer = float(config_dict["price_per_beer"])
    price_per_wine = float(config_dict["price_per_wine"])
    price_per_hard_liquor = float(config_dict["price_per_hard_liquor"])

    beer_cost = required_beer * price_per_beer
    wine_cost = required_wine * price_per_wine
    hard_liquor_cost = required_hard_liquor * price_per_hard_liquor

    total_cost = beer_cost + wine_cost + hard_liquor_cost

    return {
        "required_beer": required_beer,
        "required_wine": required_wine,
        "required_hard_liquor": required_hard_liquor,
        "beer_cost": beer_cost,
        "wine_cost": wine_cost,
        "hard_liquor_cost": hard_liquor_cost,
        "total_cost": total_cost,
    }
