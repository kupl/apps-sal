def sale_hotdogs(n):
    return n * 100 if 0 < n < 5 else n * 95 if n in range(5, 10) else n * 90
