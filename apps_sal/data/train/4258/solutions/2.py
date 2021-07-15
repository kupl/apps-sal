def series_sum(n):
    seriesSum = 0.0
    for x in range(n):
        seriesSum += 1 / (1 + x * 3)
    return '%.2f' % seriesSum
