def converter(mpg):
    km = 1.609344
    liters = 4.54609188
    return round(mpg / liters * km, 2)
