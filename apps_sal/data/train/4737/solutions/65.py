def fuel_price(liters, price):
    if liters < 2:
        return liters * price
    elif liters < 4:
        return liters * (price - 0.05)
    elif liters < 6:
        return liters * (price - 0.10)
    elif liters < 8:
        return liters * (price - 0.15)
    elif liters < 10:
        return liters * (price - 0.20)
    else:
        return liters * (price - 0.25)
