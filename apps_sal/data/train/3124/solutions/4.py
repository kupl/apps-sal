def get_exponent(n, p):
    if p <= 1:
        return None
    (x, e) = (0, 1)
    while n % e == 0:
        x += 1
        e *= p
    return x - 1
