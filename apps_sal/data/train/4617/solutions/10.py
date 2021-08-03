from typing import List


def powers_of_two(n: int) -> List[int]:
    """ Return a list of all the powers of 2 with the exponent ranging from 0 to n. """
    return [2 ** _ for _ in range(n + 1)]
