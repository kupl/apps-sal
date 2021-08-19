from itertools import takewhile, count


def halving_sum(n):
    return sum(takewhile(lambda x: x >= 1, map(lambda y: n // 2 ** y, count())))
