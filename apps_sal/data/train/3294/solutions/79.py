def converter(mpg):
    coef = 4.54609188 / 1.609344
    return round(mpg / coef, 2)
