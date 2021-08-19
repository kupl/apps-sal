def century(year):
    if year < 101:
        return 1
    if str(year)[-2:] == '00':
        return int(str(year)[:-2])
    return int(str(year)[:-2]) + 1
