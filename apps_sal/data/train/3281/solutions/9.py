import calendar 
def unlucky_days(year):
    return [calendar.weekday(year, m, 13) for m in range(1,13)].count(4)
