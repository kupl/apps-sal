def fuel_price(liters, price_per_liter):
    if liters == 0:
        return price_per_liter
    else:
        if liters >= 10:
            return round(liters * (price_per_liter - 0.25), 2)
        if liters >= 8:
            return round(liters * (price_per_liter - 0.2), 2)
        if liters >= 6:
            return round(liters * (price_per_liter - 0.15), 2)
        if liters >= 4:
            return round(liters * (price_per_liter - 0.1), 2)
        if liters >= 2:
            return round(liters * (price_per_liter - 0.5), 2)
        else:
            round(liters * price_per_liter, 2)
