def year_days(year):
    return '{0} has {1} days'.format(year, 366 if is_leap(year) else 365)


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
