def evaporator(content, evap_per_day, threshold):
    critical = content * threshold / 100
    days = 0
    while content > critical:
        days += 1
        content -= content * evap_per_day / 100
    return days
