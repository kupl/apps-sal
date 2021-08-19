def year_days(year):
    leap = 0 if year % 4 else 1
    cent = 0 if year % 100 else -1
    quad = 0 if year % 400 else 1
    return f'{year} has {365 + leap + cent + quad} days'
