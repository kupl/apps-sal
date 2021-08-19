def sumin(n):
    return sum((i * i for i in range(1, n + 1)))


def sumax(n):
    return n ** 3 - sumin(n - 1)


def sumsum(n):
    return n ** 3 + n ** 2
