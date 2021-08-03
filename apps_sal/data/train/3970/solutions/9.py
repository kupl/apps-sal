def odd_row(n):
    stop = n * (n + 1)
    return list(range(stop - n * 2 + 1, stop, 2))
