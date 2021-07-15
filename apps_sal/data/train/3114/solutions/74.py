def year_days(y):
    day = '365'
    if y%100 == 0:
        if y%400 == 0:
            day = '366'
    elif y%4==0:
        day = '366'    
    return f'{y} has {day} days'
