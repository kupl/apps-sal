def converter(mpg):
    kpl = 1.609344 / 4.54609188 * mpg
    r = round(kpl, 2)
    if type(r) is int:
        return int(r)
    elif type(r*10) is int:
        return round(r, 1)
    else:
        return r
