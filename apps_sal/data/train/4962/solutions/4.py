def days_until_christmas(day):
    christmas = date(day.year + ((day.month, day.day) > (12, 25)), 12, 25)
    return (christmas - day).days
