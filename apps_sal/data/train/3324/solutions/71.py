def sale_hotdogs(n):
    if n < 5:
        return n * 100
    elif n < 10:
        return 95 * n
    elif n >= 10:
        return 90 * n
