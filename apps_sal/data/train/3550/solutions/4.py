def sum_square_even_root_odd(nums):
    return round(sum((x ** 2 if x % 2 == 0 else x ** 0.5 for x in nums)), 2)
