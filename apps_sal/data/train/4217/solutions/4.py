from calendar import FRIDAY
from datetime import datetime


def solve(a, b):
    ds = (datetime(year, month, 1) for year in range(a, b + 1) for month in [1, 3, 5, 7, 8, 10, 12])
    ds = [d for d in ds if d.weekday() == FRIDAY]
    return format(ds[0], '%b'), format(ds[-1], '%b'), len(ds)
