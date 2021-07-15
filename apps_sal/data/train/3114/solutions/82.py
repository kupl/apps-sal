def year_days(year):
    if year%4 == 0:
        if year%100==0:
            if year%400==0:
                return '{} has 366 days'.format(year)
        else:
            return '{} has 366 days'.format(year)
  
    return '{} has 365 days'.format(year)
