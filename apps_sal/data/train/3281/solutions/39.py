import datetime

def unlucky_days(year):
    sm=0
    for i in range(1,13):
        dt=datetime.datetime(year,i,13)
        if dt.strftime("%A")=="Friday":
            sm+=1
            
    return sm
