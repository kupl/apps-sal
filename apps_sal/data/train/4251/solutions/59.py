def difference_of_squares(n):
    sum_n = 0
    sum_n2 = 0
    for i in range(1,n + 1):
        sum_n += i
        sum_n2 += i ** 2
    sum_n = sum_n ** 2
    return sum_n - sum_n2
