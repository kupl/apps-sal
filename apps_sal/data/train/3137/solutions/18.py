from math import ceil, floor


def round_it(n):
    l, r = map(len, str(abs(n)).split('.'))
    return (round, ceil, floor)[(l < r) - (l > r)](n)
