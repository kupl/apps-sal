def fib(n, a, b):
    for i in range(n):
        yield a
        a, b = b, a + b


def calc(k, n, m, x):
    if x <= 2:
        return k
    if x == 3:
        return 2 * k
    b = 2 + sum(fib(n - 4 - 1, 1, 1))
    a = 1 + sum(fib(n - 4 - 1, 1, 2))
    c = (m - b * k) // a
    b = 2 + sum(fib(x - 4, 1, 1))
    a = 1 + sum(fib(x - 4, 1, 2))
    return k * b + c * a
