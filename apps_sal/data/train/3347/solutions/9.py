def minimum(a, x):
    n = a % x
    m = (a // x + 1) * x - a
    return min(n, m)
