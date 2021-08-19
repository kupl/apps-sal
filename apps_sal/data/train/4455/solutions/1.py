def sumin(n):
    return sum(((i + 1) * (2 * (n - i) - 1) for i in range(n)))


def sumax(n):
    return sum(((n - i) * (2 * (n - i) - 1) for i in range(n)))


def sumsum(n):
    return sumin(n) + sumax(n)
