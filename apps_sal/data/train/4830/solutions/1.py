def riemann_trapezoidal(f, n, a, b):
    dx = (b - a) / n
    return round(sum(dx * (f(a + i * dx) + f(a + (i + 1) * dx)) / 2 for i in range(n)), 2)
