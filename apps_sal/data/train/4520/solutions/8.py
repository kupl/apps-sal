from heapq import nlargest
from operator import mul

def max_product(a):
    return mul(*nlargest(2,a))
