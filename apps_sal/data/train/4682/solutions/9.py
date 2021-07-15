import re

def date_correct(date):
    if not date : return date
    days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if not bool(re.match(r"\d{2}\.\d{2}\.\d{4}",date)) : return None
    d,m,y=list(map(int,date.split(".")))
    
    while m>12 or d>days[m-1]:
        y+=(m-1)//12
        m=(m-1)%12+1
        if (y%4==0 and y%100!=0) or y%400==0:
            days[1]=29
        else : days[1]=28
        if d>days[m-1]:
            d-=days[m-1]
            m+=1
            
    return "{:02}.{:02}.{}".format(d,m,y)

