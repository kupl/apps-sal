def century(year):
    year1 = year - 1 if str(year).endswith('00') else year
    return int(str(year1 + 100)[:-2])
