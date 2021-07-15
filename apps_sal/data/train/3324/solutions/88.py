def sale_hotdogs(n):
    price = 100 if n < 5 else 95 if 5 <= n and n < 10 else 90
    return n * price
