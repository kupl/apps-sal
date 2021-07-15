def approx_root(n):
    m = n**0.5
    a, b = [int(x) for x in [m, m + 1]]
    c = a**2
    return round(a + ((n - c) / (b**2 - c)), 2)
