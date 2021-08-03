def converter(mpg):
    liter_per_mile = 1.609344 / 4.54609188
    return round(liter_per_mile * mpg, 2)
