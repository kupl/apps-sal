from itertools import starmap
from operator import mul
from typing import List


def adjacent_element_product(array: List[int]) -> int:
    return max(starmap(mul, list(zip(array, array[1:]))))
