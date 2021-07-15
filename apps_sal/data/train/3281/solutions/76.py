import datetime

def unlucky_days(year):
    total = 0
    for x in range(1,13):
        if datetime.date(year,x,13).isoweekday() == 5:
            total += 1
    return total
