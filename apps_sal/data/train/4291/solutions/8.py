def century(year):
    year=year//100+bool(year%100)
    return year
