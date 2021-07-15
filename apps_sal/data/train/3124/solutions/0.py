def get_exponent(n, p):
    if p > 1:
        x = 0
        while not n % p:
            x += 1
            n //= p
        return x
