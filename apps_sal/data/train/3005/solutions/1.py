def f(n):
    (a, b) = (1, 2)
    for _ in range(n):
        (a, b) = (b, a + b)
    return a - 1
