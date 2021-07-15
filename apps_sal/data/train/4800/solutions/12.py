def hotpo(n):
    if n == 1:
        return 0
    rv = 0
    while n != 1:
        rv += 1
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
    return rv
