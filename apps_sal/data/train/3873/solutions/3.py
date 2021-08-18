from functools import reduce


def product_sans_n(nums):
    if len([x for x in nums if x == 0]) > 1:
        return [0] * len(nums)

    from operator import mul
    from functools import reduce
    onezero = 0 in nums
    product = reduce(mul, nums if not onezero else nums[:nums.index(0)] + nums[nums.index(0) + 1:])

    if onezero:
        return list(map((lambda x: 0 if x != 0 else product), nums))
    else:
        return list(map((lambda x: product / x), nums))
