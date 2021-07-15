def year_days(year):
    days=365 if year%4!=0 or (year%100==0 and (year//100)%4!=0) else 366
    return "{} has {} days".format(year,days)
