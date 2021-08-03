def fuel_price(l, price):
    if l < 2:
        return l * price
    elif l < 4:
        return l * (price - .05)
    elif l < 6:
        return l * (price - 0.10)
    elif l < 8:
        return l * (price - 0.15)
    elif l < 10:
        return l * (price - 0.20)
    else:
        return l * (price - 0.25)
