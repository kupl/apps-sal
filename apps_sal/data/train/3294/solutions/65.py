def converter(mpg):
    x = round(mpg * 1.609344 / 4.54609188, 2)
    return x if str(x)[-1] != '0' else float(str(x)[:-1])
