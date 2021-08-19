def simpson(n):
    from math import sin, pi
    a = 0
    b = pi
    h = (b - a) / n

    def f(x):
        return 3 / 2 * sin(x) ** 3
    integral = 0
    integral += f(a) + f(b)
    integral += 4 * sum((f(a + (2 * i - 1) * h) for i in range(1, n // 2 + 1)))
    integral += 2 * sum((f(a + 2 * i * h) for i in range(1, n // 2)))
    integral *= h / 3
    return integral
