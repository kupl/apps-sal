from datetime import datetime as dt
def unlucky_days(year):
    return sum(int(dt(year,x,13).weekday()==4) for x in range(1,13))
