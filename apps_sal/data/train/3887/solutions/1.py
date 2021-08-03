def f(n):
    w = 3 * n - 2
    for i in range(1, n):
        yield (str(i % 10) * n).center(w)
    line = ''.join(str(i % 10) for i in range(1, n)) + (str(n % 10) * n) + ''.join(str(i % 10) for i in reversed(range(1, n)))
    for i in range(n):
        yield line
    for i in reversed(range(1, n)):
        yield (str(i % 10) * n).center(w)


def pattern(n):
    return '\n'.join(f(n))
