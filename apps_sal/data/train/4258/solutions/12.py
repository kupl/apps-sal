def series_sum(n):
    return '{0:.2f}'.format(sum([1.0 / (1 + 3 * x) for x in range(n)]))
