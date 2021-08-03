def unlucky_days(year):
    import datetime
    weekdays_13 = [datetime.date(year, mm, 13).weekday() for mm in range(1, 13)]
    return weekdays_13.count(4)
