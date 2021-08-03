def fuel_price(l, p):
    if l <= 3:
        return round(l * p - (l * .05), 2)
    elif l <= 5:
        return round(l * p - (l * .15), 2)
    elif l <= 7:
        return round(l * p - (l * .15), 2)
    elif l <= 9:
        return round(l * p - (l * .20), 2)
    else:
        return round(l * p - (l * .25), 2)
