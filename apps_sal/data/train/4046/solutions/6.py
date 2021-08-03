from functools import reduce
from operator import mul
from math import ceil


def calculate_scrap(scraps, number_of_robots):
    return ceil(number_of_robots * 50 / reduce(mul, [(100 - s) / 100 for s in scraps]))
