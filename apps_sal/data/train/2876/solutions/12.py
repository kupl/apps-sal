from typing import List, Union


def check(array: List[Union[int, str]], value: Union[int, str]) -> bool:
    """ Check whether the provided array contains the value, without using a loop. """
    return value in array
