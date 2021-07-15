def year_days(year: int) -> str:
    """ Get the days in the given year. """
    if not year % 4:
        if not year % 100:
            if not year % 400:
                days_per_year = 366
            else:
                days_per_year = 365
        else:
            days_per_year = 366
    else:
        days_per_year = 365

    return f"{year} has {days_per_year} days"
