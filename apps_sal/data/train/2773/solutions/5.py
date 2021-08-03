import math


def calculate_years(principal, interest, tax, desired):
    return 0 if principal >= desired else math.ceil((math.log(desired) - math.log(principal)) / math.log(1 + interest * (1 - tax)))
