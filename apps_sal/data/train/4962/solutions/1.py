from datetime import date, timedelta


def days_until_christmas(day):
    next = day + timedelta(days=6)  # Increments year if between christmas and new years
    return (date(next.year, 12, 25) - day).days
