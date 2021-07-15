import datetime
def unlucky_days(y):
    return sum(datetime.date(y,i,13).weekday() == 4 for i in range(1,13))
