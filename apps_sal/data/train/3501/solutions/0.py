from math import factorial as f


def number_of_routes(m, n):
    return f(m + n) // (f(m) * f(n))
