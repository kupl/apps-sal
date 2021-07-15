def converter(mpg):
    kmpg = mpg * 1.609344
    
    kmpl = kmpg / 4.54609188
    return float(format(kmpl, '.2f'))
