def sum_square_even_root_odd(nums):
    return round(sum(n ** ((2 - n % 2) / (1 + n % 2)) for n in nums), 2)
    

