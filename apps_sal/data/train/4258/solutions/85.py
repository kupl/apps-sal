def series_sum(n):
    y = str(round(sum([1 / x for x in range(1, n * 3 + 1, 3)]), 2))
    while len(y) < 4:
        y += '0'
    return '0.00' if n == 0 else y
