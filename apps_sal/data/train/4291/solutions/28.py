def century(year):
    remainder = year % 100
    year = int(year / 100)
    if remainder > 0:
        year += 1
    return year
