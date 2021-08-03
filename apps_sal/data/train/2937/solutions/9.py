from typing import List


def between(a: int, b: int) -> List[int]:
    """ Get an array of all integers between the input parameters, including them. """
    return list(range(a, b + 1))
