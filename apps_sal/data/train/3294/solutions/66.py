def converter(mpg):
    km = mpg * 1.609344
    kpl = km / 4.54609188
    return round(kpl, 2)
