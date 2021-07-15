def sum_square_even_root_odd(nums):
    return round(sum(a ** (2, 0.5)[a % 2] for a in nums), 2)

