def series_sum(n):
    sum = 0
    for i in range(0, n):
        sum += 1.0 / (i * 3 + 1)
    return "%.2f" % sum
