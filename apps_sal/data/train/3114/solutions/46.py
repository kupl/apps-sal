def year_days(year):
    leap = 0
    if year % 4 == 0:
        leap = 1
        if year % 100 == 0 and year % 400:
            leap = 0
    return f"{year} has {366 if leap else 365} days"
