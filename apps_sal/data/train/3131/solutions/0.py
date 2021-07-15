from operator import mul
from functools import reduce


def unique_digit_products(nums):
    return len({reduce(mul, (int(a) for a in str(num))) for num in nums})

