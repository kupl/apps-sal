from math import floor, ceil


def round_it(n):

    left, right = str(n).split('.')

    if len(left) == len(right):
        return round(n)
    if len(left) > len(right):
        return floor(n)
    if len(left) < len(right):
        return ceil(n)
