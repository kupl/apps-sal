def century(year):
    if year >= 0 and year <= 100:
        return 1
    else:
        if year % 100 == 0:
            return year / 100
        else:
            return int(year / 100 + 1)
