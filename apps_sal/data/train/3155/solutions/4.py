def fit_in(a, b, m, n):
    if a + b <= max(m, n) and max(a, b) <= min(m, n):
        return True
    else:
        return False
