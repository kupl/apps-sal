from functools import reduce
import operator


def product_sans_n(nums):
    prod = reduce(operator.mul, [x for x in nums if x != 0])
    zero_count = nums.count(0)
    for index, value in enumerate(nums):
        if value != 0 and zero_count != 0:
            nums[index] = 0
        elif value == 0 and zero_count > 1:
            nums[index] = 0
        elif value == 0:
            nums[index] = prod
        else:
            nums[index] = prod // value
    return nums
