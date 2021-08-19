from datetime import datetime
FRIDAY = 4


def unlucky_days(year):
    bad_days_counter = 0
    for month in range(1, 13):
        if datetime(year, month, 13).weekday() == FRIDAY:
            bad_days_counter += 1
    return bad_days_counter
