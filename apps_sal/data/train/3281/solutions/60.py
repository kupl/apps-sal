from datetime import date

def unlucky_days(year,count=0):
    d1 = date.toordinal(date(year,1,1))
    d2 = date.toordinal(date(year,12,31))
    for i in range(d1, d2+1):
        #print(date.weekday(date.fromordinal(i)), date.fromordinal(i).day)
        if date.weekday(date.fromordinal(i)) == 4 and date.fromordinal(i).day == 13:
            count += 1
    return count
