def difference_of_squares(n):

    sum_1 = 0

    sum_2 = 0

    for num in range(1, (n + 1)):
        sum_1 += num
        sum_2 += num**2

    return ((sum_1**2) - sum_2)
