import math


def calculate_years(principal, interest, tax, desired):
    # P(1+IT)^Y = D
    return math.ceil(math.log(desired * 1.0 / principal, 1 + interest * (1 - tax)))
