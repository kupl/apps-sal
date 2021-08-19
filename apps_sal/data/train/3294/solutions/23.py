def converter(mpg):
    ldReturn = mpg / 4.54609188
    ldReturn *= 1.609344
    return float('%.2f' % ldReturn)
