import datetime
def unlucky_days(y):
    return len([i for i in range(12) if datetime.date(y,i+1,13).weekday() == 4])
