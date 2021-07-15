import heapq
from functools import reduce
from operator import mul

def max_product(a):
  return reduce(mul, heapq.nlargest(2,a))
