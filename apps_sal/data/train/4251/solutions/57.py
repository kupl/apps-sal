def difference_of_squares(n):
    square_sum, sum_square = 0, 0
    for i in range(1, n + 1):
        square_sum += i
        sum_square += i**2

    return square_sum**2 - sum_square
