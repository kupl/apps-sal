import pandas as pd
from datetime import datetime, timedelta


def unlucky_days(year):
    unlucky = 0
    start_date = datetime(year, 1, 1)
    end_date = datetime(year + 1, 1, 1)
    delta = end_date - start_date
    for i in range(delta.days + 1):
        day = start_date + timedelta(days=i)
        if ((day.strftime('%A') == "Friday") and (day.strftime('%d') == "13")):
            unlucky += 1
    return unlucky
