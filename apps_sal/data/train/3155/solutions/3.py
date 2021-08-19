def fit_in(a, b, m, n):
    if max(a, b) > min(m, n):
        return False
    if sum([a, b]) > max(m, n):
        return False
    return True
