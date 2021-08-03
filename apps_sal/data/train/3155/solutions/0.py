def fit_in(a, b, m, n):
    return max(a, b) <= min(m, n) and a + b <= max(m, n)
