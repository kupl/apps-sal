def fuel_price(l, p):
    if l <= 3:
        return round(l * p - l * 0.05, 2)
    elif l <= 5:
        return round(l * p - l * 0.15, 2)
    elif l <= 7:
        return round(l * p - l * 0.15, 2)
    elif l <= 9:
        return round(l * p - l * 0.2, 2)
    else:
        return round(l * p - l * 0.25, 2)
