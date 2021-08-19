def get_exponent(n, p):
    i = 1
    if p <= 1:
        return None
    while n % p ** i == 0:
        i += 1
    return i - 1
