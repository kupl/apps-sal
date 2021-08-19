import math


def calculate_years(principal, interest, tax, desired):
    return math.ceil(math.log(desired * 1.0 / principal, 1 + interest * (1 - tax)))
