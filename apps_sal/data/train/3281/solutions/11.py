def unlucky_days(year):
    x=0
    import datetime
    for i in range(1, 13):
        if datetime.date(year, i, 13).weekday()==4:
            x=x+1
    return x
