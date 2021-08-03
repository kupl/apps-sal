import datetime


def unlucky_days(year):
    total = 0
    month = 1
    while month < 13:
        test = datetime.datetime(year, month, 13)
        if datetime.datetime.weekday(test) == 4:
            total += 1
            month += 1
        else:
            month += 1
            continue
    return total
