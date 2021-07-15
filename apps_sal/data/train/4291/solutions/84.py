import math

def century(year):
    # year is divisible by 100
    if year % 100 == 0:
        what_century = year / 100
    # the year is not divisible by 100
    else:
        what_century = math.floor(year / 100) + 1
            
    return what_century

