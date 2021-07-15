from functools import reduce
import datetime

def unlucky_days(year):
    return  reduce(
        lambda a, b: a + (1 if datetime.datetime(year, b + 1, 13).weekday() == 4 else 0)
        , range(12), 0)
