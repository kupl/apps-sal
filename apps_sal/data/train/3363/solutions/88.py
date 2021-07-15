def evaporator(content, evap_per_day, threshold):
    threshold = content * threshold / 100
    day = 0
    while content > threshold:
        content *= 1 - evap_per_day * 0.01
        day += 1
    return day
