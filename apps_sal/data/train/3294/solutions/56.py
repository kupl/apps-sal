def converter(mpg):
    m = 1.609344
    g = 4.54609188
    res_round = round(mpg * m / g, 2)
    return res_round
