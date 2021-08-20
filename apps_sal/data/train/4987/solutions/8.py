def how_many_years(date1, date2):
    (a, b) = map(int, map(lambda x: x.split('/')[0], (date1, date2)))
    return abs(b - a)
