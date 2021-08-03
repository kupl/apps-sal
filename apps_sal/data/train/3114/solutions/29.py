def find_leapyear(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return 1
    else:
        return 0


def year_days(year):
    if find_leapyear(year):
        return f"{year} has 366 days"
    else:
        return f"{year} has 365 days"
