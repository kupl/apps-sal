import datetime as d
import calendar
def unlucky_days(year):
    l = []
    for i in range(1,13):
        l.append(calendar.monthrange(year,i)[1])
    count = 0
    for i in range(0,12):
        if l[i]>=28 and d.date(year,i+1,13).weekday() == 4:
            count+=1
    return count

