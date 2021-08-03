def century(year):
    if year % 100 == 0:
        return int(str(year)[:-2])
    elif year < 100:
        return 1
    return int(str(int(str(year)[:-2]) + 1))
