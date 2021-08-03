def evaporator(content, evap_per_day, threshold):
    days = 0
    currentLt = content
    while currentLt >= content * threshold / 100.0:
        currentLt = currentLt * (1 - evap_per_day / 100.0)
        days += 1
    return days
