import datetime


def unlucky_days(year):
    counter = 0
    for i in range(1, 13):
        d = datetime.date(year, i, 13)
        if d.weekday() == 4:
            counter += 1
    return counter
