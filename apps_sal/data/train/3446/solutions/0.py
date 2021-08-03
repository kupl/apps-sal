def approx_root(n):
    base = int(n**0.5)
    return round(base + (n - base**2) / ((base + 1)**2 - base**2), 2)
