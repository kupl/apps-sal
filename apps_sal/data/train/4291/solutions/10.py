def century(year):
    return int(year / 100) if year % 100 == 0 else int(year / 100) + 1
