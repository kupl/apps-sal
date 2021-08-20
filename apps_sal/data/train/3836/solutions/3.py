def factors(n):
    return -1 if not n or type(n) != int or n < 1 else [e for e in range(n, 0, -1) if n % e == 0]
