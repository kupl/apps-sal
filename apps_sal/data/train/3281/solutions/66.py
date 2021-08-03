def unlucky_days(year):
    from datetime import date
    unluckyday = 0
    for month in range(1, 13):
        if date(year, month, 13).weekday() == 4:
            unluckyday += 1
    return unluckyday
