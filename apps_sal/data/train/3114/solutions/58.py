def year_days(y):
    if y%100==0:
        return f'{y} has 366 days' if y%400==0 else f'{y} has 365 days'
    return f'{y} has 366 days' if y%4==0 else f'{y} has 365 days'
