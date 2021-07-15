def century(year):
    if year < 100:
        return 1
    elif year < 1000:
        return int(str(year)[0]) + 1
    else:
        return int(str(year)[:-2]) + 1 if year % 100 != 0 else int(str(year)[:-2])
