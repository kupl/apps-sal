def converter(mpg):
    '''Converts mpg to kpl. Rounds to two decimal places.'''
    kpl = round(mpg * 1.609344 / 4.54609188, 2)
    return kpl
