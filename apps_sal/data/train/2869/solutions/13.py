from typing import List


def distinct(seq: List[int]) -> List[int]:
    """ Remove duplicates from an array of numbers and return it as a result. """
    return list(dict.fromkeys(seq))
