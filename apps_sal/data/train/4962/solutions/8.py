import datetime


def days_until_christmas(today):
    noel = datetime.date(today.year, 12, 25)
    result = (noel - today).days
    return result if result >= 0 else (datetime.date(noel.year + 1, noel.month, noel.day) - today).days
