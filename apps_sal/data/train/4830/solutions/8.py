def riemann_trapezoidal(f, n, a, b):
    d = (b - a) / n
    sum = f(a) + f(b)
    for i in range(1, n):
        sum += 2 * f(a + i * d)
    return round(0.5 * sum * d, 2)
