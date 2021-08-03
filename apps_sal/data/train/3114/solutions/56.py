def year_days(year):
    y = 365
    if year % 4 == 0:
        y = 366
    if year % 100 == 0:
        if year % 400 == 0:
            y = 366
        else:
            y = 365
    return f"{year} has {y} days"
