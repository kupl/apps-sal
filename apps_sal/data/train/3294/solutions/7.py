KM_PER_MILE = 1.609344
LITERS_PER_UK_GALLON = 4.54609188


def converter(mpg):
    return round(mpg * KM_PER_MILE / LITERS_PER_UK_GALLON, 2)
