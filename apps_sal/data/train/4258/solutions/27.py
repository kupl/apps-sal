def series_sum(n):
    return "{0:.2f}".format(round(sum(1.0 / (1 + 3 * m) for m in range(n)), 2)) if n else "0.00"
