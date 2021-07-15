def series_sum(n):
    return "{:.2f}".format(sum([1 / i for i in range(1, n * 3 + 1, 3)]))
