def unlucky_days(year):
    import calendar
    fridays = 0
    for i in range(1, 13):
        if calendar.weekday(year, i, 13) == 4:
            fridays += 1
    return fridays
