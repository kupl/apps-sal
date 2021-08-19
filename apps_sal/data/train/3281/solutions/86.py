from datetime import date


def unlucky_days(year):
    day = 13
    unlucky_days_count = 0
    for x in range(1, 13):
        date_obj = date(year=year, month=x, day=day)
        if date_obj.weekday() == 4:
            unlucky_days_count += 1
    return unlucky_days_count
