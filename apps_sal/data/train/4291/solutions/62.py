def century(year):
    if year/100 <= 0:
        return 1
    elif year%100 == 0:
        return int(year/100)
    else:
        return int((year/100)+1)

