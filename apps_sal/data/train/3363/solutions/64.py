def evaporator(x, y, z):
    content = x
    evap_per_day = y / 100
    treshold = z / 100
    days = 0
    min_content = content * treshold
    while content >= min_content:
        content -= content * evap_per_day
        days += 1
    return days
