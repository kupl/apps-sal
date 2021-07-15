import datetime


def unlucky_days(year):

    counter = 0
    for i in range(1,13):
        thirteenth = datetime.date(year, i, 13)
        if thirteenth.weekday() == 4:
            counter += 1

    return counter
