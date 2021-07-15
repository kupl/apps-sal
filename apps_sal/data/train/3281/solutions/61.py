from datetime import date
def unlucky_days(year):
    NumDays=0
    for i in range(1,12+1):
        if date(year,i,13).weekday()==4:
            NumDays+=1
    return NumDays

