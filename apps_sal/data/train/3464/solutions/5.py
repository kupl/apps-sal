def isLeapYear(y):
    return (not y % 4) * bool(y % 100 + (not y % 400))
