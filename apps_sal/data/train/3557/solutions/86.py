def odd_count(n):
    g = 0
    if n % 2 != 0:
        g = (n - 1) / 2
        g + 1
    else:
        g = n / 2
    return g
