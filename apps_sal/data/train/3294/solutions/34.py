def converter(mpg):
    Imperial_Gallon = 4.54609188
    Mile = 1.609344

    kml = Mile / Imperial_Gallon
    return round(kml * mpg, 2)
