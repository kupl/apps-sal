def converter(mpg):
    gallon = 4.54609188
    mile = 1.609344
    kpl = round(mpg * mile/gallon, 2)
    return kpl

