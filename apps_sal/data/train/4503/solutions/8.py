def f(n):
    return [2 ** i if i != n + 1 else 2 ** i - 1 for i in range(n + 2)]
