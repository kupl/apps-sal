def sum_square_even_root_odd(nums):
    return round(sum([x ** 0.5 if x % 2 else x ** 2 for x in nums]), 2)
