from datetime import date


def days_until_christmas(day):
    return (date(day.year + (day.month == 12 and day.day > 25), 12, 25) - day).days
