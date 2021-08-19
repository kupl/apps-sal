def is_leap_year(year):
    if year % 4 != 0:
        return False
    if year <= 1752:
        return True
    return year % 100 != 0 or year % 400 == 0


DOM = {1: 0, 2: 31, 3: 59, 4: 90, 5: 120, 6: 151, 7: 181, 8: 212, 9: 243, 10: 273, 11: 304, 12: 334}


def is_julian_period(date, month, year):
    if year > 1752:
        return True
    if year < 1752:
        return False
    if month < 9:
        return False
    if month > 9:
        return True
    return date >= 14


def normalized_day(date, month, year):
    """Number of days between given date and an arbitrary origin. normalized_day(1, 1, 0) == 1
    """
    orig_year = 0
    days = date + DOM[month] + (year - orig_year) * 365
    if is_leap_year(year) and month >= 3:
        days += 1
    for y in range(orig_year, year, 4):
        if is_leap_year(y):
            days += 1
    if is_julian_period(date, month, year):
        days -= 11
    return days


def days(date, month, year):
    return normalized_day(24, 3, 2437) - normalized_day(date, month, year)
