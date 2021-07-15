def how_many_years (date1,date2):
    year = lambda d: int(d[:4])
    return abs(year(date1) - year(date2))
