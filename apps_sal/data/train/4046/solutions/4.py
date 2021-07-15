from fractions import Fraction as F
from math import ceil


def calculate_scrap(scraps, number_of_robots):
    cost = 50
    for pct in scraps:
        factor = F(100, 100 - pct)
        cost *= factor
    return ceil(cost * number_of_robots)
