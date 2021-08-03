from functools import reduce
from math import ceil
from operator import mul


def find_middle(string):
    try:
        n = str(reduce(mul, list(map(int, list(filter(str.isdigit, string))))))
        size = len(n)
        return int(n[ceil(size / 2 - 1):size // 2 + 1])
    except TypeError:
        return -1
