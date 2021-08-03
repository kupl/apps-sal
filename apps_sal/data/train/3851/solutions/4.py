def interest(p, r, n):
    return [round(p + p * r * n), round(p * ((1 + r)**n))]
