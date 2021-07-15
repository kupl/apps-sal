from functools import reduce
from operator import mul

def increasing_numbers(digits):
    return reduce(mul, range(digits+1, digits+10), 1) // 362880
