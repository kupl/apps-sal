def converter(mpg):
    kpl = mpg * 4.54609188 ** (-1) * 1.609344
    return round(kpl, 2)
