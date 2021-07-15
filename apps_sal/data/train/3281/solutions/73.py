from calendar import weekday
def unlucky_days(year):
    return sum(weekday(year,i,13) == 4 for i in range(1, 13))
