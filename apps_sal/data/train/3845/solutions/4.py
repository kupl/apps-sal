from functools import reduce
from operator import __mul__


def product(numbers):
    if numbers:
        return reduce(__mul__, numbers)
