from operator import mul
from functools import reduce


def product(numbers):
    if not numbers:
        return None
    return reduce(mul, numbers)
