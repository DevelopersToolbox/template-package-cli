"""
This module provides command-line argument parsing, processing, and execution functionalities for the application.

This module defines the main functions for setting up the argument parser, processing the arguments, and running the
main logic of the application. The module uses the argparse library to handle command-line arguments and the wolfsoftware.drawlines
module to draw lines for output formatting. It also utilizes the config module to create configurations from the parsed arguments.
"""

import argparse
import sys

from types import SimpleNamespace

from .config import create_configuration_from_arguments
from .globals import ARG_PARSER_DESCRIPTION, ARG_PARSER_EPILOG, ARG_PARSER_PROG_NAME, VERSION_STRING


def setup_arg_parser() -> argparse.ArgumentParser:
    """
    Set up and returns the argument parser with all required flags, optional, and required arguments.

    This function creates an ArgumentParser object and defines the available command-line arguments, including flags for help,
    debug, verbose, and version information. It also sets up optional and required argument groups for additional parameters.

    Returns:
        argparse.ArgumentParser: The configured argument parser.
    """
    parser = argparse.ArgumentParser(prog=ARG_PARSER_PROG_NAME,
                                     add_help=False,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     description=ARG_PARSER_DESCRIPTION,
                                     epilog=ARG_PARSER_EPILOG)

    flags: argparse._ArgumentGroup = parser.add_argument_group(title='flags')
    optional: argparse._ArgumentGroup = parser.add_argument_group(title='optional')
    required: argparse._ArgumentGroup = parser.add_argument_group(title='required')

    flags.add_argument("-h", "--help", action="help", default=argparse.SUPPRESS, help="Show this help message and exit")
    flags.add_argument("-d", "--debug", action="store_true", default=False, help="Enable debug mode with very noisy output")
    flags.add_argument("-v", "--verbose", action="store_true", default=False, help="Enable verbose output - show scan results as they come in")
    flags.add_argument('-V', '--version', action="version", version=VERSION_STRING, help="Show program's version number and exit.")

    optional.add_argument("-i", "--optional-integer", type=int, default=2, help="An optional integer parameter")
    optional.add_argument("-s", "--optional-string", type=str, default="me", help="An optional string parameter")

    required.add_argument("-r", "--required", type=str, required=True, help="A required parameter")

    return parser


def process_arguments(parser: argparse.ArgumentParser) -> argparse.Namespace:
    """
    Process and validates the command-line arguments.

    This function uses the provided argument parser to parse the command-line arguments. It validates the parsed arguments
    and returns them in a Namespace object.

    Args:
        parser (argparse.ArgumentParser): The argument parser to use for parsing the command-line arguments.

    Returns:
        argparse.Namespace: The parsed and validated arguments.
    """
    args: argparse.Namespace = parser.parse_args()
    return args


def run() -> None:
    """
    Master controller function.

    This function sets up the argument parser, processes the command-line arguments, creates the configuration from
    the arguments, and executes the main functionality. It handles errors related to argument parsing and exits with
    an appropriate status code in case of failure.
    """
    parser: argparse.ArgumentParser = setup_arg_parser()
    try:
        args: argparse.Namespace = process_arguments(parser)
        config: SimpleNamespace = create_configuration_from_arguments(args)
        print(f"Args: {args}")
        print(f"Config: {config}")
    except argparse.ArgumentTypeError as err:
        parser.print_usage()
        print(err)
        sys.exit(1)
