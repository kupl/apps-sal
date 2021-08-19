imperial_gallon = 4.54609188
mile = 1.609344


def converter(mpg):
    return round(mpg / imperial_gallon * mile, 2)
