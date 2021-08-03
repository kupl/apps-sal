def century(year):
    cent = year // 100
    ost = year % 100
    if ost >= 0.01:
        cent1 = cent + 1
    else:
        cent1 = cent
    return cent1
