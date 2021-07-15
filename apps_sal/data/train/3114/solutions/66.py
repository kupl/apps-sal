def year_days(y):
    return f'{y} has {365 + (1 if (not y % 4) and (y % 100 or not y % 400) else 0)} days'
