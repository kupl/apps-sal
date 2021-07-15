def evaporator(content, evap_per_day, threshold):
    days = 0
    minimum = content * threshold / 100
    while content > minimum:
        days += 1
        content -= content * evap_per_day / 100
    return days
