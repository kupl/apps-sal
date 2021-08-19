def fit_in(a, b, m, n):
    return min(m, n) >= max(a, b) and max(m, n) >= a + b
