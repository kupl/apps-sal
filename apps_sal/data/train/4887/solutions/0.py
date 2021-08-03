import datetime


def days(date, month, year):
    x = datetime.datetime(year, month, date)
    y = datetime.datetime(2437, 3, 24)
    delta = y - x
    t = delta.days
    if year < 1752 or (year == 1752 and month < 9) or (year == 1752 and month == 9 and date < 14):
        t -= 11
    if year < 1752:
        y = year // 4 * 4 + 4
        for i in range(y, 1752, 4):
            if i % 100 == 0 and i % 400 != 0:
                t += 1
    return t
