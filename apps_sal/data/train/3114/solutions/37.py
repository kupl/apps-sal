def year_days(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                d = '366'
            else:
                d = '365'
        else:
            d = '366'
    else:
        d = '365'
    return f'{year} has {d} days'
