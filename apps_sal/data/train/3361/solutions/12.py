from typing import List


def sum_of_minimums(numbers: List[int]) -> int:
    """ Find the sum of minimum value in each row. """
    return sum([min(_num_list) for _num_list in numbers])
