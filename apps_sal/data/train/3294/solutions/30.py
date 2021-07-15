def converter(mpg):
    
    miles_to_km = 1.609344
    gallon_to_liter = 4.54609188
    
    return round((mpg / gallon_to_liter) * miles_to_km,2)

