GALLON_LITRE_RATE = 4.54609188
MILE_KM_RATE = 1.609344


def converter(mpg):
    return round(mpg / GALLON_LITRE_RATE * MILE_KM_RATE, 2)
