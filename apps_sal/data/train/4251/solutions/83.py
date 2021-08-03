def difference_of_squares(n):
    sum_1 = 0
    sum_2 = 0
    for i in range(1, n + 1):
        sum_1 = sum_1 + (i * i)
    for i in range(1, n + 1):
        sum_2 = sum_2 + i
    return ((sum_2 * sum_2) - sum_1)
