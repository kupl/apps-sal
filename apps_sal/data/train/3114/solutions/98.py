def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def year_days(year):
    if is_leap(abs(year)):
        return '{} has {} days'.format(year, 366)
    return '{} has {} days'.format(year, 365)
