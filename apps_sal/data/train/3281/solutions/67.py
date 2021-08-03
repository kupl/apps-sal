import datetime


def unlucky_days(year):
    friday_13 = 0
    months = range(1, 13)
    for i in months:
        if datetime.date(year, i, 13).weekday() == 4:
            friday_13 += 1
    return friday_13
