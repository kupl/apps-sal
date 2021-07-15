def survivor(n):
    d = 2
    while n >= d:
        if n % d == 0: return False
        n -= n // d
        d += 1
    return True
