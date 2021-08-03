def riemann_trapezoidal(f, n, a, b):
    s = 0
    d = (b - a) / n
    for i in range(n):
        x = a + i * d
        y = x + d
        s += (f(x) + f(y)) * d / 2
    return round(s, 2)
