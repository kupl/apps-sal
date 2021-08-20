def lucasnum(n):
    (a, b) = (2, 1)
    for i in range(abs(n)):
        (a, b) = (b, a + b)
    return a * (-1 if n < 0 and n % 2 else 1)
