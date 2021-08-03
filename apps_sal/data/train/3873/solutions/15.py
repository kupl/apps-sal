from functools import reduce


def product_sans_n(nums):
    if nums.count(0) > 1:
        return [0] * len(nums)
    if nums.count(0) == 1:
        i = nums.index(0)
        s = reduce(int.__mul__, nums[:i] + nums[i + 1:])
    t = reduce(int.__mul__, nums)
    return [s if x == 0 else t // x for x in nums]
