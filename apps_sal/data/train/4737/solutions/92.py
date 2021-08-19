def fuel_price(l, p):
    """ Candian Gas Sale"""
    return round(l * (p - l // 2 * 0.05), 2) if l < 12 else round(l * (p - 0.25), 2)
