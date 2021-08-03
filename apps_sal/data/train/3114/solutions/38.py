def year_days(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return str(year) + ' has ' + str(366) + ' days'

            else:
                return str(year) + ' has ' + str(365) + ' days'
        else:
            return str(year) + ' has ' + str(366) + ' days'
    else:
        return str(year) + ' has ' + str(365) + ' days'
