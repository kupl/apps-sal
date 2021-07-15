def zeros(n):
    b = 0
    while 5 ** b < n:
        b += 1
    return sum(n // (5 ** c) for c in range(1, b))
