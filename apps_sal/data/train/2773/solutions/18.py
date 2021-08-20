import math


def calculate_years(principal, interest, tax, desired):
    return -1 if principal < 0 else math.ceil(math.log(float(desired) / principal if principal else 1, 1 + interest * (1 - tax)))
