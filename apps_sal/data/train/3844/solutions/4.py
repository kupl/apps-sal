from functools import reduce
from itertools import combinations


def poly_from_roots(r):
    return [sum((reduce(lambda x, y: -x * y, c, 1) for c in combinations(r, i))) for i in range(len(r), -1, -1)]
