from typing import Tuple


def triple_trouble(*args: Tuple[str]) -> str:
    """ Get a string that combines all of the letters of the three inputed strings in groups. """
    return ''.join(list(map(''.join, zip(*args))))
