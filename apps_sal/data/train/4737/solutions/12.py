def fuel_price(l, p):
    dic = {(0, 1): p, (2, 3): p - 0.05, (4, 5): p - 0.1, (6, 7): p - 0.15, (8, 9): p - 0.2}
    return round(l * dic.get(max((i if l in i else (0, 0) for i in dic)), p - 0.25), 2)


def fuel_price(l, p):
    return round(l * next((d for (a, d) in [(10, p - 0.25), (8, p - 0.2), (6, p - 0.15), (4, p - 0.1), (2, p - 0.05), (0, p)] if l >= a)), 2)
