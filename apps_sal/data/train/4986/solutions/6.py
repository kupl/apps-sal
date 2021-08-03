def f(n, m):
    k = n // m
    r = n % m
    return (m * (m - 1) // 2) * k + r * (r + 1) // 2
