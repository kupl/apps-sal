from functools import reduce
from operator import __mul__


def greatest_product(n):
    return max([reduce(__mul__, list(map(int, x))) for x in [x for x in [n[i:i + 5] for i in range(len(n))] if len(x) == 5]])
