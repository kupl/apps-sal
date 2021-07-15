def sum_square_even_root_odd(nums):
    return round(sum(n ** 2 if n % 2 == 0 else n ** 0.5 for n in nums), 2)
