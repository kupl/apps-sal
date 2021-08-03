def evaporator(content, evap_per_day, threshold):
    e = evap_per_day / 100
    t = threshold / 100
    h = (content * t)
    days = 0
    while content > h:
        content = content * (1 - e)
        days += 1

    return (days)
