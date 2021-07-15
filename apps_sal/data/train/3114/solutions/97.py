def year_days(year):
    day =  year % 100 == 0 and year % 400 == 0 or not year % 100 == 0 and year % 4 == 0
    days = 5, 6    
    years = f'{year} has 36{days[day]} days'
    return years
