def sum_square_even_root_odd(nums):
    return round(sum(i**[2, 0.5][i & 1] for i in nums), 2)
