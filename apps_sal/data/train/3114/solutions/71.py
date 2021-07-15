def year_days(year):
    d=365
    if year % 100 == 0:
        if year % 400 == 0: #is leap
            d=366
    elif year % 4 == 0:
        d=366
    return str(year) + ' has ' + str(d) + ' days'
