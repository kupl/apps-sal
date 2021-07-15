def century(year):
    century = year/100
    if century.is_integer() == False:
        century = int(century) + 1
    return century
