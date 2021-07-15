def converter(mpg):
    t1, t2 = (4.54609188, 1.609344)
    return round(mpg * t2 / t1, 2)
