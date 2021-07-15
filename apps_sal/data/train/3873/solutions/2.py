from functools import reduce
from operator import mul

def mulsum(xs):
    return reduce(mul, xs, 1)

def product_sans_n(nums):
    nz = nums.count(0)
    if nz > 1:
        return [0] * len(nums)
    elif nz:
        return [0 if x else mulsum([_f for _f in nums if _f]) for x in nums]
    xs = mulsum(nums)
    return [xs // x for x in nums]

