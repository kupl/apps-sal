def days_until_christmas(day):
    return (date(day.year + (1 if day.month > 11 and day.day > 25 else 0), 12, 25) - day).days
