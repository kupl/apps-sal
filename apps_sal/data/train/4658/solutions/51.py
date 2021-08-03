from functools import reduce
from operator import mul
def max_product(l, n): return reduce(mul, sorted(l, reverse=True)[:n])
