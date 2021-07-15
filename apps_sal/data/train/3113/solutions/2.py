def distribute(m, n):
    m = max(0, m)
    return [m // n + (m % n > i) for i in range(n)]
