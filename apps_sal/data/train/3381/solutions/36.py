def get_real_floor(n):
    if 1 <= n <= 12:
        n = n - 1
    elif 14 <= n:
        n = n - 2
    else:
        n = n

    return n
