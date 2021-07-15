def hotpo(n):
    c = 0
    next_n = n
    while next_n != 1:
        if next_n % 2 == 0:
            next_n = next_n / 2
        else:
            next_n = next_n * 3 + 1
        c += 1
    else:
        return c
