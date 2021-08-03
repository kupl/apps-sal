import math


def calculate_years(principal, interest, tax, desired):
    x = (float(desired) / float(principal))
    base = (1 + (float(interest) * (1 - float(tax))))
    years = math.log(x, base)
    return math.ceil(years)
