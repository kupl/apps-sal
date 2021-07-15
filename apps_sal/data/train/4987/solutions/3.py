def how_many_years (date1, date2):
    get_year = lambda date: int(date.split('/')[0])
    return abs(get_year(date1) - get_year(date2))
