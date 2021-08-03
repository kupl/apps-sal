from typing import List


def gimme(array: List[int]) -> int:
    """ Get the index of the numerical element that lies between the other two elements. """
    return array.index(next(iter({*array} - ({min(array), max(array)}))))
