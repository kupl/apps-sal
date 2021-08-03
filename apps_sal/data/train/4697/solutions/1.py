from functools import reduce
from operator import and_
from collections import Counter


def common(a, b, c):
    return sum(reduce(and_, map(Counter, (a, b, c))).elements())
