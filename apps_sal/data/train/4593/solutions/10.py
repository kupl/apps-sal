from typing import List

def merge_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
    """ Merge two sorted arrays into one and return it. """
    return sorted(set(arr1 + arr2))
