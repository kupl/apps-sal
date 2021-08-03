from itertools import takewhile, count
from operator import truth


def zeros(n):
    return sum(takewhile(truth, (n // 5 ** e for e in count(1))))
