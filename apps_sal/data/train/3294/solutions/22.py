def converter(mpg):
    conversion_factor = 1.609344 / 4.54609188
    kpl = mpg * conversion_factor
    return round(kpl, 2)
