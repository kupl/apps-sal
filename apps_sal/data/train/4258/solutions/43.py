def series_sum(n):
    return "{0:.2f}".format(sum([(1 + 3 * (k - 1))**-1 if k > 0 else k for k in range(n + 1)]))
