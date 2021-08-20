import calendar
import datetime


def unlucky_days(year):
    start_date = datetime.date(year, 1, 1)
    end_date = datetime.date(year, 12, 31)
    delta = datetime.timedelta(days=1)
    counter = 0
    while start_date <= end_date:
        year = int(str(start_date)[:4])
        month = int(str(start_date)[5:7])
        day = int(str(start_date)[8:10])
        if day == 13 and calendar.weekday(year, month, day) == 4:
            counter += 1
        start_date += delta
    return counter
