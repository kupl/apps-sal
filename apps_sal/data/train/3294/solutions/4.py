def converter(mpg):
    gallon_to_liter_rate = 4.54609188
    mile_to_km_rate = 1.609344
    return round(mpg * mile_to_km_rate / gallon_to_liter_rate, 2)
