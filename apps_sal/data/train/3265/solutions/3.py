from math import ceil


def mult_triangle(n):
    s = (n * (n + 1) / 2)**2
    odd = ceil(n / 2)**4
    return [s, s - odd, odd]
