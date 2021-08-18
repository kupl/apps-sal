def series_sum(n):
    f = 3 * n - 2
    s = 0
    if n == 0:
        return "0.00"
    for i in range(1, f + 1, 3):
        s = s + (1 / i)
    return "{:.2f}".format(s)
