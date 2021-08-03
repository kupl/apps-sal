def hotpo(n):
    if n == 1:
        return 0
    x = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n) + 1
        x += 1
    return x
