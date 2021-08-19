from itertools import combinations
from functools import reduce
from operator import mul


def poly_from_roots(r):
    res = []
    for p in range(len(r) + 1):
        factor = sum((reduce(mul, [v for v in k], 1) for k in combinations(r, p)))
        res.append(-factor if p % 2 else factor)
    return res[::-1]
