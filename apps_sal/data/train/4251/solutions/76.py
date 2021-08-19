def difference_of_squares(n):
    sum1 = 0
    sum2 = 0
    for i in range(n + 1):
        sum1 += i ** 2
        sum2 += i
    return sum2 ** 2 - sum1
