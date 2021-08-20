def difference_of_squares(n):
    sum_of_squares = 0
    square_of_sum = 0
    for i in range(1, n + 1):
        square_of_sum += i
        sum_of_squares += i ** 2
    return square_of_sum ** 2 - sum_of_squares
