from math import sqrt
from itertools import permutations


def sort_by_perfsq(a):
    return sorted(a, key=lambda n: (-sum((str(sqrt(int(''.join(p))))[-2:] == '.0' for p in set(permutations(str(n), len(str(n)))))), n))
