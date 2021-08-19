def hotpo(n):
    i = 0
    j = 0
    if n == 1:
        j = 1
    while j != 1:
        if n % 2 == 0:
            n = n / 2
            i += 1
            if n == 1:
                j = 1
        elif n % 2 != 0:
            n = 3 * n + 1
            i += 1
            if n == 1:
                j = 1
    return i
