import datetime
def unlucky_days(year):
    unlucky = 0
    for month in range(1,13):
        if datetime.datetime(year,month, 13).weekday() == 4:
            unlucky += 1
    return unlucky
