from math import exp


def ex_euler(n):
    def f(x, y): return 2 - exp(-4 * x) - 2 * y
    def exact(x): return 1 + 0.5 * exp(-4 * x) - 0.5 * exp(-2 * x)
    x, y, T = 0, 1, 1
    h = T / n
    mx = [0]
    for _ in range(n):
        y += h * f(x, y)
        x += h
        z = exact(x)
        mx.append(abs(y - z) / z)
    return float(str(sum(mx) / (n + 1))[:8])
