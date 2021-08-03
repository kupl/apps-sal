def series_sum(n):
    return "%.2f" % sum([1 / (1 + (3 * t)) for t in range(n)])
