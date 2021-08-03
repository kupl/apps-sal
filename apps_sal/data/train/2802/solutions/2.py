from functools import reduce
from operator import mul


def per(n):
    results = []
    while n > 9:
        n = reduce(mul, map(int, str(n)))
        results.append(n)

    return results
