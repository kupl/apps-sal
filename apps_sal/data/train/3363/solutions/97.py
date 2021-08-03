def evaporator(content, evap_per_day, threshold):
    days = 0
    volume_threshold = content * (threshold / 100)
    while content > volume_threshold:
        content -= content * (evap_per_day / 100)
        days += 1
    return days
