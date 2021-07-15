def converter(mpg):
    M =1.609344
    g =  4.54609188
    kpg = (mpg *M)/g
    return round(kpg,2)
