from functools import reduce
from operator import mul


def product(numbers):
    return reduce(mul, numbers) if numbers else None
