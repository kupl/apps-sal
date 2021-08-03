def sale_hotdogs(n):
    return 0 if n == 0 else n * 100 if n < 5 else n * 95 if n < 10 else n * 90
