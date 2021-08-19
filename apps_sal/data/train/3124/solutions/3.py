def get_exponent(n, p):
    return next(iter((i for i in range(int(abs(n) ** (1 / p)), 0, -1) if n / p ** i % 1 == 0)), 0) if p > 1 else None
