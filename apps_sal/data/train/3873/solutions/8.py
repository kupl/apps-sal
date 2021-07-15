from functools import reduce


def product_sans_n(nums):
    zero, prod = nums.count(0), reduce(int.__mul__, (n for n in nums if n))
    if zero:
        return [0 for _ in nums] if zero > 1 else [0 if n else prod for n in nums]
    return [prod // n for n in nums]
