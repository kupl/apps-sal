from functools import reduce
from math import floor, gcd, sqrt

def smallest_factor(n):
    return next((d for d in range(2, floor(sqrt(n)) + 1) if n % d == 0), n)

def scf(nums):
    return 1 if nums == [] else smallest_factor(reduce(gcd, nums))
