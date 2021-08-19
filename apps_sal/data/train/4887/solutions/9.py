from datetime import date

'''Datetime assumes "the current Gregorian calendar always 
   was, and always will be, in effect."'''
GREG_START = date(1752, 9, 14)
GREG_SKIP = 11
CURR_DATE = date(2437, 3, 24)


def days(day, month, year):
    try:
        target_date = date(year, month, day)
        distance = (CURR_DATE - target_date).days
    except ValueError:  # Gregorian/Julian conflict
        target_date = date(year, month, day - 1)
        distance = (CURR_DATE - target_date).days - 1
    if target_date < GREG_START:
        distance -= GREG_SKIP
        distance += len([cent for cent in range((year - 1) // 100 + 1, GREG_START.year // 100 + 1) if cent % 4])
    return distance
