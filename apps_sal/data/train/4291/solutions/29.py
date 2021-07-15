def century(year):
    counter = 0
    while year >= 1:
        year = year - 100
        counter = counter + 1
    return counter
