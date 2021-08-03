from typing import List


def sum_of_minimums(numbers: List[int]) -> int:
    """ Find the sum of minimum value in each row. """
    return sum(map(min, numbers))
