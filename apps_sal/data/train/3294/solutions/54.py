def converter(mpg):
    KM_PER_MILE = 1.609344
    LITRE_PER_GALLON = 4.54609188
    tmp = round((mpg * KM_PER_MILE / LITRE_PER_GALLON), 2) * 100
    return (tmp // 10) / 10 if tmp % 10 == 0 else tmp / 100
