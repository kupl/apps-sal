def difference_of_squares(n):
    squares_sum = sum([i for i in range(1, n + 1)])**2
    sum_squares = sum([i**2 for i in range(1, n + 1)])
    return squares_sum - sum_squares
