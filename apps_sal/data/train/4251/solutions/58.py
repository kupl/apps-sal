def difference_of_squares(n):
    sum_n_range = sum([i for i in range(n+1)])**2
    square_n_range = sum([i**2 for i in range(n+1)])
    return sum_n_range - square_n_range
