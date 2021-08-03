def hotpo(n):
    x = 0
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
        x += 1
    return x
