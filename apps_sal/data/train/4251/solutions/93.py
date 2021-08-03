def difference_of_squares(n):
    # ...
    sq_of_sum = sum(i for i in range(n + 1))**2
    sum_of_sq = sum(i**2 for i in range(n + 1))

    return sq_of_sum - sum_of_sq
