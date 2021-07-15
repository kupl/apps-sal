def converter(mpg):
    lr, km = 1.609344, 4.54609188
    return round(mpg * (lr / km), 2)
