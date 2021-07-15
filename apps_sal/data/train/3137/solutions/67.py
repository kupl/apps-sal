import math

def round_it(n):
    nums = str(n).split('.')
    if len(nums[0]) == len(nums[1]):
        return round(n)
    elif len(nums[0]) < len(nums[1]):
        return math.ceil(n)
    else:
        return math.floor(n)
