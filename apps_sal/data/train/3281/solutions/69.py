import calendar

def unlucky_days(year):
    n = 0
    for i in range (1,13):
        if calendar.weekday(year, i, 13) == 4:
            n += 1
    return n
