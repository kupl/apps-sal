def number_increasing(n):
    if n == 1:
        return True
    if (n - 1) % 5 == 0:
        return True
    t = 3
    while t <= n:
        if t == n or (n - t) % 5 == 0:
            return True
        t *= 3
    return False
