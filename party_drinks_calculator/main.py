"""Contains the main function."""

import yaml
from .calculate import calculate_liquor_quantities
from .io import print_welcome_message, get_users_values, print_results
from .runtime_args import parse_runtime_args


def main():
    """The main function."""
    # Get runtime args
    cli_args = parse_runtime_args()

    # Parse config file
    with open(cli_args.config, "r") as config_file:
        config_dict = yaml.load(config_file)

    # Say "welcome"!
    print_welcome_message(config_dict)
    print()

    # Get values from the user
    user_dict = get_users_values()
    print()

    # Get our results
    results_dict = calculate_liquor_quantities(
        config_dict, user_dict, rounding_method=cli_args.rounding
    )

    # Print the results
    print_results(config_dict, results_dict)
