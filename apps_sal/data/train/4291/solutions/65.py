def century(year):
    
    yearOne = str(year)
    length = len(yearOne)
    lastTwo = int(yearOne[length - 2: length])
    
    if lastTwo > 0:
        century = int(((year - lastTwo) + 100) / 100)
    else:
        century = int((year - lastTwo) / 100 )

    return century
