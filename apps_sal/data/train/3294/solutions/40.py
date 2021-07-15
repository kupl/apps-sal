def converter(mpg):
    mile = 1.609344
    gallon = 4.54609188
    kpl = mpg * mile / gallon
    return round(kpl, 2)
