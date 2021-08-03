def converter(mpg):
    mpk = 4.54609188 / 1.609344
    return round(mpg / mpk, 2)
