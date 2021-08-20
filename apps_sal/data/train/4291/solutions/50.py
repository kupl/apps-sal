def century(year):
    anul = int(year)
    secol = int(anul / 100 + 1)
    if anul % 100 == 0:
        secol_1 = secol - 1
        return secol_1
    else:
        return secol
