def evaporator(content, evap_per_day, threshold):
    day_count = 0
    percentage_to_ml = content * threshold / 100
    while content >= percentage_to_ml:
        day_count += 1
        content -= content * evap_per_day / 100
    return day_count
