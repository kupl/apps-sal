def year_days(y):
    return  f'{y} has {[365,366][y%4==0 and (y%400==0 or y%100!=0)]} days'
