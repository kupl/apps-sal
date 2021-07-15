def sale_hotdogs(n):
    if 0 < n < 5:
        return 100 * n
    if n >= 5 and n < 10:
        return 95 * n
    if n >= 10:
        return 90 * n
    return 0
