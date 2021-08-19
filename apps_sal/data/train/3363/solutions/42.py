def evaporator(content, evap_per_day, threshold):
    days = 0
    current = content
    while content * threshold / 100 < current:
        current *= 1 - evap_per_day / 100
        days += 1
    return days
