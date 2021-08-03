def extra_perfect(n):
    n = n if n % 2 != 0 else n - 1
    F = []
    i = 0
    while 2 * i + 1 <= n:
        F.append(2 * i + 1)
        i += 1
    return F
