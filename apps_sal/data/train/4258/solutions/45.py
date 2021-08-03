def series_sum(n):
    total = 0
    for num in range(1, n + 1):
        total += (1 / (1 + (3 * (num - 1))))
    return "%.2f" % total
