def converter(mpg):
    kof = 4.54609188 / 1.609344
    a = mpg / kof
    return round(a, 2)
    # your code here
