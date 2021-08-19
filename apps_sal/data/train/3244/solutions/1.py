def f(n, v):
    return n / v - n % v / v


def cheapest_quote(n):
    return round(n * 0.1 - (f(n, 5) + f(n, 10) + f(n, 20) + f(n, 40)) * 0.01, 2)
