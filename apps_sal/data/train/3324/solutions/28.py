def sale_hotdogs(n):
    if 0 < n < 5:
        return 100 * n
    elif 5 <= n < 10:
        return 95 * n
    elif n >= 10:
        return 90 * n
    return 0
