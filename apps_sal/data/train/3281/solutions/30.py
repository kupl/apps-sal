import datetime as dt

def unlucky_days(y):
    return sum(dt.datetime(y, i+1, 13).weekday() == 4 for i in range(12))


