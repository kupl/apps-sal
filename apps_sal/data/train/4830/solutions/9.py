def riemann_trapezoidal(f, n, a, b):
    ret = 0.5 * (f(b) + f(a))
    h = (b - a) / n
    for i in range(1, n):
        ret += f(a + i * h)
    ret = (ret * h * 100 + 0.5) // 1 / 100
    return ret
