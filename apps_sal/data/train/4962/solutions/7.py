def days_until_christmas(day):
    CHRISTMAS = date(day.year,12,25)
    if day > CHRISTMAS:
        CHRISTMAS = CHRISTMAS.replace(year=day.year + 1)
    return (CHRISTMAS - day).days
