def year_days(y):
    """
    leap year calculator
    """
    return "{} has {} days".format(y, [365, 366, 365, 366][(y % 4 == 0) + (y % 100 == 0) + (y % 400 == 0)])
