def fuel_price(l, price):
    if l < 2:
        return l * price
    elif l < 4:
        return l * (price - 0.05)
    elif l < 6:
        return l * (price - 0.1)
    elif l < 8:
        return l * (price - 0.15)
    elif l < 10:
        return l * (price - 0.2)
    else:
        return l * (price - 0.25)
