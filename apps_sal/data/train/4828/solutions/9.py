def count_squareable(n):
    q, r = divmod(n, 4)
    if r < 2:
        num = 3 * q + r
    else:
        num = 3 * q + r - 1
    return num
