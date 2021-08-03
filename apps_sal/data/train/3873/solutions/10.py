from functools import reduce


def product_sans_n(nums):
    if nums.count(0) > 1:
        return [0 for i in nums]
    elif nums.count(0) == 1:
        prod = reduce(lambda a, b: a * b, [x for x in nums if x != 0])
        return [0 if i != 0 else prod for i in nums]
    else:
        prod = reduce(lambda a, b: a * b, nums)
        return [prod // i for i in nums]
