from operator import mul
from functools import reduce
(base, n) = ({1}, 1)
for _ in range(2000):
    n += reduce(mul, map(int, str(n).replace('0', '')))
    base.add(n)


def convergence(n):
    steps = 0
    while n not in base:
        n += reduce(mul, map(int, str(n).replace('0', '')))
        steps += 1
    return steps
