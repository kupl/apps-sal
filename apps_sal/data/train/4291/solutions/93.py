def century(year):
    if year < 100:
        return 1
    return int(str(year)[:-2]) + 1 if str(year)[-2:] > '00' else int(str(year)[:-2])
