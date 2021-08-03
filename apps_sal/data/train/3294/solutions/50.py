def converter(mpg):
    l = 4.54609188
    k = 1.609344
    kpl = k / l * mpg
    return round(kpl, 2)
