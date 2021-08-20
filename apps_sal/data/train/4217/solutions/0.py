from calendar import month_abbr
from datetime import datetime


def solve(a, b):
    res = [month_abbr[month] for year in range(a, b + 1) for month in [1, 3, 5, 7, 8, 10, 12] if datetime(year, month, 1).weekday() == 4]
    return (res[0], res[-1], len(res))
