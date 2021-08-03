def rocks(n):
    l = len(str(n))
    return int(n + 1 - 10**(l - 1)) * l + sum(9 * i * 10**(i - 1) for i in range(l))
