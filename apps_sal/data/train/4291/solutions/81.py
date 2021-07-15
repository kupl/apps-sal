def century(year):
    count = 0
    while(year > 0):
        count += 1
        year = year-100
    return count

