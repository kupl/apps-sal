from operator import mul, abs
from functools import reduce

def find_difference(a, b):    
    return abs(reduce(mul,a) - reduce(mul,b))
