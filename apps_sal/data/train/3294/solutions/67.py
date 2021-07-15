def converter(mpg):
    km = mpg * (1.609344) 
    kml = km / 4.54609188
    return round(kml, 2)
