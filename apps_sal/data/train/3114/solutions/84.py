def year_days(year):
    mystr = str()
    if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
        days_in_year = 366
    else:
        days_in_year = 365
    mystr = str(year) + " has " + str(days_in_year) + " days"
    return mystr
