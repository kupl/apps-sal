def hotpo(n):
    i = 0
    x = n
    while x != 1:
        i += 1
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3 * x + 1
    return 0 if n == 1 else i
