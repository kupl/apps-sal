def sale_hotdogs(n):
    return ((n < 5) * 100 * n) + ((n >= 5 and n < 10) * 95 * n) + ((n >= 10) * 90 * n)
