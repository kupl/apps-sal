def sum_square_even_root_odd(nums):
    return round(sum((n ** (0.5 if n % 2 else 2) for n in nums)), 2)
