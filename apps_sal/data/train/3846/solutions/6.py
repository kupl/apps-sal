def f(k, n):
    (g, r, c) = ([], 1, 0)
    for i in range(n // k):
        c += k * r
        g.append(r)
        r += g[(i + 1) // k]
    return c + r * (n % k + 1)
