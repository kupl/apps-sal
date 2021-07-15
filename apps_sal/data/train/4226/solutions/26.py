from itertools import count, filterfalse
from typing import List

def remove_smallest(numbers: List[int]) -> List[int]:
    """
    Remove the smallest value from the array of the integers. Obey the following rules:
    - If there are multiple elements with the same value, remove the one with a lower index
    - If you get an empty array/list, return an empty array/list
    """
    return list(filterfalse(lambda _it, c=count(): _it == min(numbers) and next(c) < 1, numbers))
