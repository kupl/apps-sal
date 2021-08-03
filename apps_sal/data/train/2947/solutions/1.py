def rounding(n, m):
    down, up = (n // m) * m, (n // m) * m + m
    if up - n < n - down:
        return up
    elif up - n == n - down:
        return n
    return down
