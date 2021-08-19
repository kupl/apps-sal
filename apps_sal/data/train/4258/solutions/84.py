def series_sum(n):
    sum = 0.0
    value = 1.0
    if n == 0:
        return format(sum, '.2f')
    for i in range(1, n + 1):
        sum = sum + 1 / value
        value += 3
    result = float('{0:.2f}'.format(sum))
    return format(sum, '.2f')
