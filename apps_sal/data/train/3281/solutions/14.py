from datetime import date


def unlucky_days(year):
    black_fridays = 0
    for month in range(1, 13):
        if date(year, month, 13).isoweekday() == 5:
            black_fridays += 1
    return black_fridays
