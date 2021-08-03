def difference_of_squares(n):
    n_sum = 0
    sum_of_squares = 0
    for number in range(n + 1):
        n_sum += number
        sum_of_squares += number ** 2
    square_of_sum = n_sum ** 2
    return square_of_sum - sum_of_squares
