def evaporator(content, evap_per_day, threshold):
    limit = content * threshold / 100
    days = 0
    while content > limit:
        days += 1
        content = content - content * evap_per_day / 100
    return days
