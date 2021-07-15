import datetime
def unlucky_days(year):
    return sum(1 for month in range(1,13) if datetime.date(year, month, 13).isoweekday() == 5)

