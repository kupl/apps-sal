def fuel_price(l, p):
    if l >= 2 and l < 4:
        return l * (p - 0.05)
    elif l >= 4 and l < 6:
        return l * (p - 0.10)
    elif l >= 6 and l < 8:
        return l * (p - 0.15)
    elif l >= 8 and l < 10:
        return l * (p - 0.20)
    return l * (p - 0.25)
