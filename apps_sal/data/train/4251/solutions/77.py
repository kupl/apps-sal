def difference_of_squares(n):
    sum_sqr = 0
    sum_sqrs = 0
    for n in range(1, n + 1):
        sum_sqr += n
        sum_sqrs += n ** 2
    sum_sqr = sum_sqr ** 2
    return sum_sqr - sum_sqrs
