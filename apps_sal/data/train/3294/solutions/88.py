def converter(mpg):
    return round(mpg * 1.609344 / 4.54609188, 2) if str(round(mpg * 1.609344 / 4.54609188, 2))[-1] != 0 else round(mpg * 1.609344 / 4.54609188, 1)
