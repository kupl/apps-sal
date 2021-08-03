def century(year):
    if year >= 100 and year % 100 == 0:
        return int(year / 100)
    elif year >= 100:
        return int(year / 100) + 1
    else:
        return 1
