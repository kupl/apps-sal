def series_sum(n):
    if n == 0:
        return "0.00"
    elif n == 1:
        return "1.00"

    sum = 1.0
    for i in range(1, n):
        sum += 1 / (1 + 3 * i)
    return '%.2f' % sum
