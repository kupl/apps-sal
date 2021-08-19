def series_sum(n):
    sum = 0
    for i in range(1, n * 3, 3):
        sum += 1 / i
    return '{:.2f}'.format(sum)
