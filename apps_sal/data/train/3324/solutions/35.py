def sale_hotdogs(n):
    if n < 5:
        return 100 * n
    elif 5 <= n < 10:
        return 95 * n
    else:
        return n * 90
