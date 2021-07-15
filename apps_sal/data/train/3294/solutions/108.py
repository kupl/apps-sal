def converter(mpg):
    lpg = 4.54609188
    kpm = 1.609344
    n = mpg * kpm / lpg
    return float(str('{:.2f}'.format(n)).rstrip('0'))
