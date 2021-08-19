def unlucky_days(year):
    from datetime import datetime as dt
    count = 0
    for i in range(1, 13):
        if dt(year, i, 13).weekday() == 4:
            count += 1
    return count
