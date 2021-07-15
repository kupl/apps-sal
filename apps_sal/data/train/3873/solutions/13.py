from functools import reduce

def product_sans_n(nums):
    zeroes = nums.count(0)
    if zeroes >= 2:
        return [0 for x in nums]
    elif zeroes == 1:
        prod = reduce(int.__mul__, (x for x in nums if x != 0))
        return [0 if x != 0 else prod for x in nums]
    
    prod = reduce(int.__mul__, nums)
    return [prod // x for x in nums]

