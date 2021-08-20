import math


def round_it(num):
    (left, right) = str(num).split('.')
    if len(left) < len(right):
        return math.ceil(num)
    if len(left) > len(right):
        return math.floor(num)
    if len(left) == len(right):
        return round(num)
