def sumin(n):
    return n * (n + 1) * (2 * n + 1) / 6


def sumax(n):
    return n * (n + 1) * (2 * n + 1) / 3 - n * (n + 1) / 2


def sumsum(n):
    return sumax(n) + sumin(n)
