def riemann_trapezoidal(f, n, a, b):
    d = (b - a) / n
    total = 0
    for i in range(n):
        hl = f(a + d * i)
        hr = f(a + d * (i + 1))
        total += d * hl + d * (hr - hl) / 2
    return round(total, 2)
