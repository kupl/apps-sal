def century(year):
    centuryCount = 0
    while year > 0:
        year -= 100;
        centuryCount = centuryCount + 1
    return centuryCount
