from numpy import array
from typing import List


def invert(lst: List[int]) -> List[int]:
    """ Get the additive inverse of each number in given list. """
    return list(-array(lst))
