from operator import mul
from functools import reduce

def product_sans_n(nums):
    z = nums.count(0)
    p = 0 if z > 1 else reduce(mul, (x for x in nums if x != 0), 1)
    return [p//x if x != 0 and z == 0 else
            p    if x == 0 and z == 1 else
            0    for x in nums]
