def series_sum(n):
    float_sum = sum([1 / (i * 3.0 + 1) for i in range(n)])
    return '%.2f' % float_sum
