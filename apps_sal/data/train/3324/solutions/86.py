def sale_hotdogs(n):
    return n * (90 if n >= 10 else 95  if 5 <= n < 10 else 100)
