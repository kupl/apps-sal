def sale_hotdogs(n):
    if n == 0:
        return 0
    if n < 5:
        return 100 * n
    return 90 * n if n >= 10 else 95 * n
