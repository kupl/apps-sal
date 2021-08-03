def year_days(y):
    leap = 0
    if y % 400 == 0:
        leap = 1
    elif y % 4 == 0 and y % 100 != 0:
        leap = 1
    return '{} has {} days'.format(y, 365 + leap)
