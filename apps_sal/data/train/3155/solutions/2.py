def fit_in(a, b, m, n):
    if m < a + b and n < a + b:
        return False
    if m < max([a, b]) or n < max([a, b]):
        return False
    return True
