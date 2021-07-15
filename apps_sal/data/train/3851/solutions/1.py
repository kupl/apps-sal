def interest(p, r, n):
    return [round(p * i) for i in ((1 + (r * n)), (1 + r)**n)]
