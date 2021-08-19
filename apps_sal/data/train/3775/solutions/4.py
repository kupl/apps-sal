from typing import Union
from re import findall


def digits(number: Union[int, str]) -> int:
    """ Get number of digits in given number. """
    return len(findall('\\d', str(number)))
