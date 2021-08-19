from math import floor, ceil


def two_decimal_places(number):
    if number >= 0:
        return floor(number * 100) / 100
    else:
        return ceil(number * 100) / 100
