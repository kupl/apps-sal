def days(date, month, year):
    daysaway = 0
    monthdays = 0
    leapyear = 0
    monthsinyear = [31,28,31,30,31,30,31,31,30,31,30,31] 

    daysaway += 24- date

    if year < 2437:
        daysaway += (2437 - year) * 365

    if month < 3:
        if month == 1:
            daysaway += monthsinyear[0] + monthsinyear[1]
        else:
            daysaway += monthsinyear[1] 
    elif month > 3:
        for i in range(3,month):
            monthdays -= monthsinyear[i-1]
        daysaway += monthdays

    if year < 1752 or (year == 1752 and month < 9) or (year == 1752 and month == 9 and date < 3):
        daysaway -= 11

    for i in range(year,2438):
        if i <= 1752 and i % 4 == 0:
            leapyear += 1
            if i==year and month > 2:
                leapyear -=1
        elif i > 1752:
            if i % 400 == 0 or (i % 4 == 0 and i % 100 !=  0):
                leapyear += 1
                if i==year and month > 2:
                    leapyear -=1
    daysaway += leapyear
    
    return daysaway
