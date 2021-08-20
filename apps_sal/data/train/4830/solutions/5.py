def riemann_trapezoidal(f, n, a, b):
    dx = (b - a) / n
    y = sum((f(a + i * dx) / (2 if i in [0, n] else 1) for i in range(n + 1)))
    return round(y * dx, 2)
