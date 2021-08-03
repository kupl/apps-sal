def converter(mpg):
    gallit = 1.609344 / 4.54609188
    lit = round(mpg * gallit, 2)
    return lit
