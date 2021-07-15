from functools import reduce
from itertools import product
from operator import mul

def solve(arr):
    xss = [[min(a), max(a)] for a in arr]
    return max(reduce(mul, xs) for xs in product(*xss))
