import math

def sum_square_even_root_odd(nums):
    return float('%.2f' % sum([x*x if x%2 == 0 else math.sqrt(x) for x in nums]))

