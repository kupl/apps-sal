from datetime import date
def unlucky_days(year):
    thirteenths=[]
    for m in range(1,13):
        if date(year,m,13).weekday()==4:
            thirteenths.append(m)
        else:
            continue
    return len(thirteenths)
