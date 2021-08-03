from typing import List


def merge_arrays(first: List[int], second: List[int]):
    """ Merge two sorted arrays into a single sorted array. """
    return sorted(set(first + second))
