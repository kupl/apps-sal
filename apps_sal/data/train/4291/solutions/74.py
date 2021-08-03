def century(year):
    siglo = 0
    if year < 100:
        siglo = 1
    else:
        siglo = year // 100
        uno = year % 100
        if uno >= 1:
            siglo += 1

    return siglo
