from typing import Tuple

def combine_names(*args: Tuple[str]) -> str:
    """ Get a full name containing two parameters (first and last name). """
    return " ".join(args)
