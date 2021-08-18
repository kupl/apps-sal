def f(n, v):
    return n / v - (n % v) / v


def cheapest_quote(n):
    return round(n * .1 - (f(n, 5) + f(n, 10) + f(n, 20) + f(n, 40)) * .01, 2)
