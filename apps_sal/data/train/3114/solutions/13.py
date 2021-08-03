from calendar import isleap


def year_days(year: int) -> str:
    """ Get the days in the given year. """
    return f"{year} has {366 if isleap(year) else 365} days"
