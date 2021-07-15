def odd_row(n):
    m = (n - 1) * n + 1
    return [*range(m, m + n * 2, 2)]
