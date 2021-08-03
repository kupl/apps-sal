def unlucky_days(year):
    from datetime import datetime

    fridays = 0

    for i in range(1, 13):
        if datetime(year, i, 13).weekday() == 4:
            fridays += 1

    return fridays
