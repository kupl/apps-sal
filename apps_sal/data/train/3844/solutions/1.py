from collections import Counter
from itertools import product
from functools import reduce
from operator import mul


class P(Counter):

    def __mul__(self, other):
        m = P()
        for ((ao, av), (bo, bv)) in product(self.items(), other.items()):
            m[ao + bo] += av * bv
        return m


def poly_from_roots(roots):
    result = reduce(mul, (P({0: -r, 1: 1}) for r in roots), P({0: 1}))
    return [result[i] for i in range(len(roots) + 1)]
