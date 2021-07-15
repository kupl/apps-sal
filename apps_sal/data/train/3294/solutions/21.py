def converter(mpg):
    litre = 4.54609188
    mile = 1.609344
    return round(mpg * mile / litre, 2)
