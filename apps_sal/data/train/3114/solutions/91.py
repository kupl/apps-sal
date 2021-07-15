def year_days(year):
    if year%100 == 0 :
        return '{} has 366 days'.format(year)  if year%400 == 0 else '{} has 365 days'.format(year)
    elif year%4 == 0:
        return '{} has 366 days'.format(year)
    else:
        return '{} has 365 days'.format(year)


