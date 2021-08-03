def converter(mpg):
    gln = 4.54609188
    ml = 1.609344
    return round(mpg * ml / gln, 2)
