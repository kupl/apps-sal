def series_sum(n):
    if n == 0:
        return '0.00'
    sum = 1.0
    count = 4
    for i in range(n - 1):
        sum += 1 / count
        count += 3
    return '{:.2f}'.format(sum, 2)
