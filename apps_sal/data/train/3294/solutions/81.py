def converter(mpg):
    # your code here
    # mpg is number of miles/1 gallon
    # 1 mpg is 1.609344/4.54609188
    a = mpg * 1.609344 / 4.54609188
    return(round(a, 2))
