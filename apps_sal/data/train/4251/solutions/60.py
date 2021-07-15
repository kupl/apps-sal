def difference_of_squares(n):
    sum_num = 0
    sum_squares = 0
    for i in range(1, n + 1):
        sum_num = sum_num + i
        sum_squares = sum_squares + i ** 2
    return sum_num ** 2 - sum_squares
