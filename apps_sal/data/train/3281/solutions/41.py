import datetime


def unlucky_days(year):
    i = 0
    for item in range(1, 13):
        day = datetime.date(year, item, 13).isoweekday()
        if day == 5:
            i += 1
    return i
