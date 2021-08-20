def c(n):
    m = 0
    while n > 0:
        n = n // 2
        m += n
    return m


def subsets_parity(n, k):
    return 'EVEN' if c(n) - c(k) - c(n - k) > 0 else 'ODD'
