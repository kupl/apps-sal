def sale_hotdogs(n):
    if n == 0:
        return 0
    elif n < 5:
        return 100 * n
    elif n >= 10:
        return 90 * n
    else:
        return 95 * n
