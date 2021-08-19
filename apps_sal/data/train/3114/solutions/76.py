def year_days(year):
    nb_days = 366 if year % 400 == 0 or (year % 4 == 0 and (not year % 100 == 0)) else 365
    return f'{year} has {nb_days} days'
