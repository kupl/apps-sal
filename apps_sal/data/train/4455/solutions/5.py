def sumin(n):
    return sum(((1 + i) * i // 2 + i * (n - i) for i in range(1, n + 1)))


def sumax(n):
    return sum((i * i + (i + 1 + n) * (n - i) // 2 for i in range(1, n + 1)))


def sumsum(n):
    return sumin(n) + sumax(n)
