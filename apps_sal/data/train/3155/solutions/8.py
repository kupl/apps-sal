def fit_in(a, b, m, n):
    return a + b <= max(m, n) and min(m, n) >= max(a, b)
