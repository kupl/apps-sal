from functools import reduce
from operator import mul
max_product=lambda l, n: reduce(mul,sorted(l, reverse=True)[:n])
