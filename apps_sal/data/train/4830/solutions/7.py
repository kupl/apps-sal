def riemann_trapezoidal(f, n, a, b):
    dx = (b - a) / n
    return round(dx * sum((sum((f(a + (i + di) * dx) for di in (0, 1))) / 2 for i in range(n))), 2)
