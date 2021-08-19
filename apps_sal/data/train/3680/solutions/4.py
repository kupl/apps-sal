def factorial(n):
    if n > 0:
        return reduce(lambda x, y: x * y, range(1, n + 1))
    if n < 0:
        return None
    return 1
