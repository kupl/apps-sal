from functools import reduce
from math import gcd


def lcm(x, y):
    return x * y // gcd(x, y)


def min_special_mult(arr):
    try:
        return abs(reduce(lcm, map(int, filter(None, arr))))
    except ValueError:
        errors = [x for x in arr if type(x) != int and (not (type(x) == str and x.isdigit()))]
        if len(errors) == 1:
            return f'There is 1 invalid entry: {errors[0]}'
        return f'There are {len(errors)} invalid entries: {errors}'
