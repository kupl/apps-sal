from datetime import date


def days_until_christmas(day):
    this_christmas = date(day.year, 12, 25)
    next_christmas = date(day.year + 1, 12, 25)
    return (this_christmas - day if day <= this_christmas else next_christmas - day).days
