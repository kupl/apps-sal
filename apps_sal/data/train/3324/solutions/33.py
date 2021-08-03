def sale_hotdogs(n):
    return n * (100 - (0 if n < 5 else 5 if n < 10 else 10))
