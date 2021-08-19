from functools import reduce
from operator import mul
from math import ceil


def calculate_scrap(scraps, number_of_robots):
    return ceil(50 * number_of_robots * 100 ** len(scraps) / reduce(mul, (100 - x for x in scraps)))
