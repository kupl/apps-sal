from operator import eq
from itertools import compress


def first_non_consecutive(a):
    return next(compress(a, [not eq(*x) for x in zip(a, list(range(a[0], a[0] + len(a) + 1)))]), None)
