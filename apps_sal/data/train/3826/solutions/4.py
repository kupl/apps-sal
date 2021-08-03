def cycle(n):
    if n % 2 == 0 or n % 5 == 0:
        return -1
    m = 1
    for p in range(1, n):
        m = 10 * m % n
        if m == 1:
            return p
