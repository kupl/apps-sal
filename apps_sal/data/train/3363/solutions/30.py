def evaporator(content, evap_per_day, threshold):
    rem = content * 0.01 * threshold
    count = 0
    while content >= rem:
        content -= content * 0.01 * evap_per_day
        count += 1
    return count

