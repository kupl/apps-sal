import datetime
def unlucky_days(year):
    sum = 0
    for month in range(1,13):
        date = datetime.datetime(year,month,13).strftime("%w")
        if date == '5':
            sum += 1
    return sum
