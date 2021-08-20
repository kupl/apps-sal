def interest(p, r, n):
    a = round(p + n * p * r)
    b = round(p * (1 + r) ** n)
    return [a, b]
