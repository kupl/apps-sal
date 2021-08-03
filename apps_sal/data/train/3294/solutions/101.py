MILE = 1.609344
GALLON = 4.54609188


def converter(mpg):
    return round(mpg / GALLON * MILE, 2)
