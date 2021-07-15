from functools import reduce
from operator import mul
from typing import List


def max_product(lst: List[int], n_largest_elements: int) -> int:
    return reduce(mul, sorted(lst)[-n_largest_elements:])

