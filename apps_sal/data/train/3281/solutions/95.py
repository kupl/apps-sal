import datetime


def unlucky_days(year):
    total = 0
    for i in range(12):
        date = datetime.datetime(year, i + 1, 13)
        if date.weekday() == 4:
            total += 1
    return total
