from operator import mul
from heapq import nlargest
from functools import reduce

def max_product(l,n):
    return reduce(mul,nlargest(n,l))
