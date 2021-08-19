from functools import reduce
from operator import mul
BASE = ord('A') - 1


def ride(group, comet):
    (g, c) = [[ord(c) - BASE for c in xs] for xs in [group, comet]]
    return 'GO' if reduce(mul, g) % 47 == reduce(mul, c) % 47 else 'STAY'
