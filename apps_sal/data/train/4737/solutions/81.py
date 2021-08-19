def fuel_price(l, p):
    return l * p - l * min(0.25, l // 2 * 5 * 0.01)
