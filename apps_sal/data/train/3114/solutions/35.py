def year_days(y):
    # your code here
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        return "{} has 366 days".format(y)
    return "{} has 365 days".format(y)
