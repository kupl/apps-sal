from math import ceil, log


def calculate_years(principal, interest, tax, desired):
    return ceil(log(float(desired) / principal, 1 + interest * (1 - tax)))
