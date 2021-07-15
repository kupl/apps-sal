from datetime import date
def unlucky_days(year):    
    counter = 0 
    for months in range(1,13):
        if date(year, months, 13).weekday()==4:
            counter +=1            
    return counter


