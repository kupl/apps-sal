import math
from functools import lru_cache


@lru_cache(maxsize=1024)
def solutions(c):
    cube = c ** 3
    return sum(1 for a in range(1, int((cube // 2)**.5) + 1) if ((cube - a**2)**.5).is_integer())


def find_abc_sumsqcube(c_max, num_sol):
    result = []
    for c in range(2, c_max + 1):
        if solutions(c) == num_sol:
            result.append(c)
    return result
