def interest(p, r, n):
    return [round(p + p * r * n), compound(p, r, n)]


def compound(p, r, n):
    return round(p) if n < 1 else compound(p + p * r, r, n - 1)
