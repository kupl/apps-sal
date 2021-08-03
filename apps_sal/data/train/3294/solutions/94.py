def converter(mpg):
    conversionFactor = 1.609344 / 4.54609188
    return round(mpg * conversionFactor, 2)
