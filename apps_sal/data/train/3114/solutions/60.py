def is_leap_year(year):
    year = abs(year)
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True

    return False


def year_days(year):
    if is_leap_year(year):
        return f"{year} has 366 days"
    else:
        return f"{year} has 365 days"
