from itertools import repeat
from functools import reduce
from operator import sub
from math import gcd


def finding_k(arr):
    return reduce(gcd, filter(None, map(sub, set(arr), repeat(min(arr)))), 0) or -1
