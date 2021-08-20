def sale_hotdogs(n):
    price = 90 if n >= 10 else 100 if n < 5 else 95
    return n * price
