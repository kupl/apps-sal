def odd_row(n):
    return [x for x in range(n * n - n, n * n + n) if x % 2 != 0]
