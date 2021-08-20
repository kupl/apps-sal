def shift_left(a, b):
    (m, n, i) = (len(a), len(b), -1)
    while m > 0 and n > 0 and (a[i] == b[i]):
        (i, m, n) = (i - 1, m - 1, n - 1)
    return m + n
