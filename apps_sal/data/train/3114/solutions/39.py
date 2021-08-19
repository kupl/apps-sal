def year_days(y):
    d = '365' if y % 4 or (y % 100 == 0 and y % 400 != 0) else '366'
    return f'{y} has {d} days'
