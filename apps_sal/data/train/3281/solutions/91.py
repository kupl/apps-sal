from calendar import weekday as wd
def unlucky_days(year):
    day=13;k=0
    for month in range(1,13):
        if wd(year,month,day)==4:
            k+=1
    return k
