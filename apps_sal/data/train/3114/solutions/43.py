def year_days(year):
    if year%400 == 0: return '{} has 366 days'.format(year)
    if year%100 == 0: return '{} has 365 days'.format(year)
    if year%4   == 0: return '{} has 366 days'.format(year)
    else            : return '{} has 365 days'.format(year)
