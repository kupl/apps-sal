from calendar import isleap

def year_days(year):
    return f"{year} has {365 + isleap(year)} days"
