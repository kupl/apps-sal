def f(n): return list(g(n))


def g(n):
    v = 1
    for i in range(n + 1):
        yield v
        v *= 2
    yield v - 1
