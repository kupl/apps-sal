def series_sum(n):
    sum_ = sum([1 / (i*3-2) for i in range(1, n+1)])
    return '%.2f' % sum_
