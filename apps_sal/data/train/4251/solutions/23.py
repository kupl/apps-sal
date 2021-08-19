def difference_of_squares(n):
    sum1 = 0
    sum2 = 0
    for x in range(n):
        sum1 += x + 1
        sum2 += (x + 1) ** 2
    return sum1 ** 2 - sum2
