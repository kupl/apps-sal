def century(year):
    century = 1
    yearCount = 100
    if year < 101:
        return 1
    else:
        while yearCount < year:
            yearCount = yearCount + 100
            century = century + 1
    return century
    return
