def converter(mpg):
    km_in_mile = 1.609344
    litres_in_gallon = 4.54609188
    return round(mpg * km_in_mile / litres_in_gallon, 2)
