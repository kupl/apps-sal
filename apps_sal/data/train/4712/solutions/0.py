def lucasnum(n):
    a = 2
    b = 1

    flip = n < 0 and n % 2 != 0

    for _ in range(abs(n)):
        a, b = b, a + b

    return -a if flip else a
