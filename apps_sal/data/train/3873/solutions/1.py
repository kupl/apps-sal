from functools import reduce


def product_sans_n(nums):
    z, p = nums.count(0), reduce(int.__mul__, (n for n in nums if n))
    return [0 for _ in nums] if z > 1 else [0 if n else p for n in nums] if z else [p // n for n in nums]
