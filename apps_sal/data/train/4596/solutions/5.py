from itertools import permutations
from collections import Counter
from math import factorial
from functools import reduce


def perms(e):
    if isinstance(e, int):
        return perms(str(e))

    c = Counter(e)

    return factorial(len(e)) / reduce(lambda x, y: x * y, [factorial(x) for x in list(c.values())])
