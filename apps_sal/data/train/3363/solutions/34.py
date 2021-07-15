def evaporator(content, evap_per_day, threshold):
    limit = content * threshold/100
    days = 0
    while content > limit:
        content -= content * evap_per_day/100
        days += 1
    return days
