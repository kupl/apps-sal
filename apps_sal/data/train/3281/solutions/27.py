from datetime import datetime


def unlucky_days(year):
    return sum((1 for x in range(1, 13) if datetime(year, x, 13).strftime('%a') == 'Fri'))
