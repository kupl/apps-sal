def converter(mpg):
    conv = 1.609344 / 4.54609188
    return float('{:.2f}'.format(mpg * conv))
