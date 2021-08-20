def how_many_years(date1, date2):

    def year(d):
        return int(d[:4])
    return abs(year(date1) - year(date2))
