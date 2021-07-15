def sale_hotdogs(n):
    return n * 100 if n < 5 else 95 * n if 10 > n >= 5 else 90 * n
