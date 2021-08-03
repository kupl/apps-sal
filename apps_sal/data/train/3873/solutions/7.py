from functools import reduce


def product_sans_n(nums):
    s = set(nums)
    if 0 in s:
        return [reduce(int.__mul__, nums[:i] + nums[i + 1:]) for i, e in enumerate(nums)]
    else:
        prod = reduce(int.__mul__, nums)
        return [prod // n for n in nums]
