def sale_hotdogs(n):
    if n < 5:
        return 100 * n
    if 10 > n >= 5:
        return 95 * n
    if n >= 10:
        return 90 * n
    else:
        return 0
