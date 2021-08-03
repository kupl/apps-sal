def rounding(n, m):
    diff = n % m

    if diff < m / 2:
        return n - diff
    elif diff > m / 2:
        return n - diff + m
    return n
