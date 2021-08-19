def century(year):
    century = 0
    for interval in range(0, year, 100):
        century += 1
    return century
