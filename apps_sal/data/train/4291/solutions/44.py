def century(year):
    if (year / 100).is_integer():
        return year / 100
    else:
        return int(year / 100) + 1
