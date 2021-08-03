from datetime import date, timedelta


def unlucky_days(year):
    d = date(year, 1, 1)
    d += timedelta(days=4 - d.weekday())
    counter = 0

    while d.year != year + 1:
        if d.weekday() == 4 and d.day == 13:
            counter += 1
        d += timedelta(days=7)

    return counter
