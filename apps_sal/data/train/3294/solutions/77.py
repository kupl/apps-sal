def converter(mpg):
    """convert miles per imperial gallon into kilometers per liter"""
    kpl = round(mpg * 1.609344 / 4.54609188, 2)
    return kpl
