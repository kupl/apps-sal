# Let's do this without the builtin date library
# and without looking up formulas in wikipedia

def is_leap_year(year):
    if year % 4 != 0:
        return False
    # year is divisible by 4.
    # If the year is in the Gregorian calendar, that's it
    if year <= 1752:
        return True
    
    # Julian calendar rule
    return (year % 100 != 0) or (year % 400 == 0)

# Day number of the first day of the month, minus one.
# Doesn't count leap years.
DOM = {
    1: 0,
    2: 31,
    3: 59,
    4: 90,
    5: 120,
    6: 151,
    7: 181,
    8: 212,
    9: 243,
    10: 273,
    11: 304,
    12: 334,
}

def is_julian_period(date, month, year):
    if year > 1752: return True
    if year < 1752: return False
    # year == 1752
    if month < 9: return False
    if month > 9: return True
    return date >= 14

# This could be rewritten as a one-liner (see wikipedia) but I'm not sure that I can derive the formula.
def normalized_day(date, month, year):
    """Number of days between given date and an arbitrary origin. normalized_day(1, 1, 0) == 1
    """
    orig_year = 0
    days = date + DOM[month] + (year - orig_year) * 365
    
    # Leap year adjustment for the current year
    if is_leap_year(year) and month >= 3:
        days += 1
    # Leap year adjustment for the intervening years
    # It could be done without a loop (count 4-year intervals,
    # subtract centuries, re-add 400-years) but it would be less
    # readable given the Gregorian stuff.
    for y in range(orig_year, year, 4):
        if is_leap_year(y):
            days += 1
    # Gregorian->Julian transition adjustment
    if is_julian_period(date, month, year):
        days -= 11
    
    return days
    
def days(date, month, year):
    return normalized_day(24, 3, 2437) - normalized_day(date, month, year)
