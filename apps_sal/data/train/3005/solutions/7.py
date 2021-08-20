def f(n):
    (a, b) = (1, 1)
    for _ in range(n + 1):
        (a, b) = (b, a + b)
    return a - 1
