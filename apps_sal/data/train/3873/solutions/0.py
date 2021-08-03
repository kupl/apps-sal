from functools import reduce


def product_sans_n(nums):
    z = nums.count(0)
    if z > 1:
        return [0] * len(nums)

    p = reduce(int.__mul__, (v for v in nums if v))
    return [not v and p for v in nums] if z else [p // v for v in nums]
