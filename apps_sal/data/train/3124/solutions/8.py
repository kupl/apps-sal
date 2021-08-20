def get_exponent(n, p):
    r = 0
    while n % p ** r == 0 and p > 1:
        r += 1
    if r > 0:
        return r - 1
