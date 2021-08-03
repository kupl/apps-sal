from math import e


def ex_euler(n):
    x, y, h, r = 0, 1, 1 / n, [1]
    for _ in range(n):
        f = 2 - e**(-4 * x) - 2 * y
        yy = y + h * f
        r.append(yy)
        x, y = x + h, yy

    real = [(1 + .5 * e**(-4 * x * h) - .5 * e**(-2 * x * h)) for x in range(n + 1)]
    err = [abs(i - j) / j for i, j in zip(r, real)]
    return float(str(sum(err) / (n + 1))[:8])
