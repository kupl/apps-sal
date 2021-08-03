from calendar import isleap


def year_days(year):
    return f"{year} has {366 if isleap(year) else 365} days"
