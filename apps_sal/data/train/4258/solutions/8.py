def series_sum(n):
    sum = 0
    for i in range(n):
        sum += 1 / (1 + 3 * i)
    return '%.2f' % sum


print((series_sum(0)))
