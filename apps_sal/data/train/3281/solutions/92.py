from datetime import timedelta, date

def unlucky_days(year):
    day_td = timedelta(days=1)
    date_i = date(year,1,1)
    
    unlucky_counter = 0
    
    for i in range(366):
        date_i = date_i + day_td
        if date_i.day == 13 and date_i.weekday() == 4:
            unlucky_counter += 1
    return unlucky_counter
