def converter(mpg):
    miles_to_km = 1.609344
    gallon_to_litre = 4.54609188
    return round(mpg * miles_to_km / gallon_to_litre, 2)
