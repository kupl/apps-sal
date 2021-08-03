def fit_in(a, b, m, n):
    return a + b <= max(m, n) and max(a, b) <= min(m, n)
