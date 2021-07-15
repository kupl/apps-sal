def difference_of_squares(n):
    sum = 0
    sum_square = 0
    num = 1
    for i in range(n):
        sum += num
        sum_square += num*num
        num += 1
    return sum**2 - sum_square

