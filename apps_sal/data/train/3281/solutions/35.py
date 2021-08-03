import datetime


def unlucky_days(year):
    howmany = 0
    for i in range(1, 13):
        day = datetime.datetime(year, i, 13)
        if day.weekday() == 4:
            howmany += 1
    return howmany
