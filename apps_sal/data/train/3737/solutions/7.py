from itertools import cycle
from operator import mul

muls = (1, 1, 3, 1, -1, 3, 1, 1, 3, -1, 1, 3, 1, 1, -3)


def calc(a):
    return sum(map(mul, map(lambda n: n * n if n > 0 else n, a), cycle(muls)))
