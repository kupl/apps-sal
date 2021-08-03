from math import ceil


def movie(c, t, p):
    n = 1
    while ceil(c + p * t * ((p ** n - 1) / (p - 1))) >= n * t:
        n += 1
    return n
