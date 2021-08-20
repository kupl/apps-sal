def paperwork(n, m):
    if n < 0:
        return 0
    elif m < 0:
        return 0
    elif n or m > 0:
        return n * m
