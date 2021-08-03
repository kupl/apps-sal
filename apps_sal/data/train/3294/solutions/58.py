def converter(mpg):
    litres = 4.54609188
    km = 1.609344
    kpl = km / litres * mpg
    return round(kpl, 2)
