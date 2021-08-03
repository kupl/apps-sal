def triangular_sum(n):
    r = int((n * 2)**0.5)
    return r * (r + 1) / 2 == n and round(r**0.5)**2 == r
