from functools import reduce
from operator import concat


def min_value(digits):
    return int(reduce(concat, map(str, sorted(set(digits)))))
