def f(n):
    if n:
        return n - m(f(n - 1))
    return 1


def m(n):
    if n:
        return n - f(m(n - 1))
    return 0
