#!/usr/bin/env python
"""This is the summary line.

This is the further elaboration of the docstring. Within this section,
you can elaborate further on details as appropriate for the situation.
Notice that the summary and the elaboration is separated by a blank new
line.
"""
import sys

from .cli import run
from .notify import system


def main() -> None:
    """
    Execute the main routine of the script.

    This function serves as the entry point of the script. It is responsible
    for invoking the `process_arguments` function, which handles the processing
    of command-line arguments. The `main` function does not take any parameters
    and does not return any value. It ensures that the script's functionality
    is triggered correctly when the script is executed.
    """
    try:
        run()
    except KeyboardInterrupt:
        system("\n[*] Exiting Program\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
