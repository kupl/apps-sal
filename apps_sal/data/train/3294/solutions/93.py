def converter(mpg):
    imperial_gallon_in_litres = 4.54609188
    mile_in_km = 1.609344
    kpl = mpg * mile_in_km / imperial_gallon_in_litres
    return float('{0:.2f}'.format(kpl))
