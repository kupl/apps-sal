def lucasnum(n):
    if n == 1:
        return 1
    elif n == 0:
        return 2
    elif n > 1:
        (a, b) = (2, 1)
        for i in range(n):
            (a, b) = (b, a + b)
        return a
    else:
        (a, b) = (-1, -2)
        for i in range(abs(n)):
            (a, b) = (b, a - b)
        return b * -1
