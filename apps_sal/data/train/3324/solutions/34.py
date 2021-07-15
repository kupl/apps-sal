def sale_hotdogs(n):
    if n == 0: return 0
    if n < 5: return n * 100
    return 95* n if 10 > n >= 5 else 90 * n 
