import calendar

def isLeapYear(year):
    # if calendar is not available:
    # return year % 4 == 0 and year and (year % 400 == 0 or year % 100 != 0)
    return calendar.isleap(year)
