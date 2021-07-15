def year_days(year):
    leap = False
    if year % 100 == 0:
        if year % 400 == 0:
            leap = True
    elif year % 4 == 0:
        leap = True        
    
    return str(year) + ' has ' + str([365, 366][leap]) + ' days'
