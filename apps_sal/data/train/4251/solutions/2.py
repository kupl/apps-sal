def difference_of_squares(x):
    square_sum = 0
    sum_squares = 0
    for i in range(1, x + 1):
        square_sum += i
        sum_squares += i ** 2
    square_sum **= 2
    return square_sum - sum_squares
