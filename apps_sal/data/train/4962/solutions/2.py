def days_until_christmas(dt):
    is_after = int(dt.month == 12 and dt.day > 25)
    christmas = dt.replace(month=12, day=25, year=dt.year + is_after)
    return (christmas - dt).days
