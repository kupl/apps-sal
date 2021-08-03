import math


def exact_sol(t):
    return 1 + 0.5 * math.exp(-4 * t) - 0.5 * math.exp(-2 * t)


def slope(y, t):
    return 2 - math.exp(-4 * t) - 2 * y


def ex_euler(n):
    y = 1
    t = 0
    error = abs(y - exact_sol(t)) / exact_sol(t)
    for _ in range(n):
        y += slope(y, t) * (1 / n)
        t += 1 / n
        error += abs(y - exact_sol(t)) / exact_sol(t)

    return (int((error / (n + 1)) * 1e6)) / 1e6
