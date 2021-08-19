from datetime import datetime


def how_many_years(*dates):
    (d1, d2) = [datetime.strptime(s, '%Y/%m/%d') for s in dates]
    return abs(d2.year - d1.year)
