# https://en.wikipedia.org/wiki/Square_pyramidal_number
def sumin(n):
    return n * (n + 1) * (2 * n + 1) / 6


def sumax(n):
    return n * (n + 1) * (4 * n - 1) / 6


def sumsum(n):
    return sumin(n) + sumax(n)
