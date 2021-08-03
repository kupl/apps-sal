def array_madness(a, b):
    a_sqr = [x**2 for x in a]
    b_cub = [y**3 for y in b]
    a_sum = sum(a_sqr)
    b_sum = sum(b_cub)
    return True if a_sum > b_sum else False
