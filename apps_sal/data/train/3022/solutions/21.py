from typing import List

def two_highest(_array: List[int]) -> List[int]:
    """ Get two max (and unique) values in the given list and return them sorted from highest to lowest. """
    return sorted(set(_array), reverse=True)[:2]
