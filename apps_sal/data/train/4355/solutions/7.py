from math import exp

def ex_euler(n):
    dx = 1 / n
    def f(x, y):
        return 2 - exp(-4*x) - 2*y
    def z(x, y):
        return 1 + 0.5*exp(-4*x) - 0.5*exp(-2*x)
    x, y = 0, 1
    errors = []
    for _ in range(n + 1):
        errors.append(abs(y - z(x, y)) / z(x, y))
        y += f(x, y)*dx
        x += dx
    return float(str(sum(errors) / (n + 1))[:8])
