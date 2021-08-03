def sale_hotdogs(n):
    return n * [90, 95, 100][(n < 10) + (n < 5)]
