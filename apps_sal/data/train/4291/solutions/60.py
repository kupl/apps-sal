def century(year):
    x = 0
    count = 0
    while year > x:
        x = x + 100
        count = count + 1
    return count
