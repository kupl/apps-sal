def lucasnum(n):
    (a, b, i) = (2, 1, 0)
    while True:
        if i == n:
            return a
        if n > 0:
            i += 1
            (a, b) = (b, a + b)
        else:
            i -= 1
            (b, a) = (a, b - a)
