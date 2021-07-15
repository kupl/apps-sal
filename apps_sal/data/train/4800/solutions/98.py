def hotpo(n):
    i = 0
    while n > 1:
        if n % 2:
            n = 3 * n + 1
        else:
            n //= 2
        i += 1
    return i
