def century(year):
    year = year / 100
    if year.is_integer():
        return int(year)
    elif isinstance(year, float):
        years = year + 1
        return int(years)
