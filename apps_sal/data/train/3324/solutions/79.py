def sale_hotdogs(n):
    if n < 5:
        return 100 * n
    elif n >= 5 and n < 10:
        return n * 95
    else:
        return 90 * n
