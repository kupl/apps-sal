from itertools import combinations, chain
from math import log
def nth_chandos_number(n):
    l = [0] + [5 ** i for i in range(1, int(log(n, 5)) + 10)]
    m = chain(*[combinations(l, ni) for ni in range(1, len(l) + 1)])
    ls = sorted(list(set([sum(i) for i in m])))
    return ls[n]

