def difference_of_squares(n):
    sum1 = 1
    sum2 = 1
    i = 1
    while i < n:
        sum1 += i + 1
        sum2 += (i + 1) ** 2
        i += 1
    return sum1 ** 2 - sum2
