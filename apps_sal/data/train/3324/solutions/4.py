def sale_hotdogs(n):
    return n * (n < 5 and 100 or n < 10 and 95 or 90)
