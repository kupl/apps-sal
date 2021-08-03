def hotpo(n):
    a = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        a += 1
    return a
