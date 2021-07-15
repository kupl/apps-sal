def get_exponent(n, p, i = 0):
    if p <= 1: return None
    return get_exponent(n / p, p, i + 1) if n / p == n // p else i
