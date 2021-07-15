import calendar

def unlucky_days(year):
    c = calendar.Calendar()
    return sum(sum(sum(list(c.yeardays2calendar(year,width=12)), []), []), []).count((13,4))
