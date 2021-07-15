def evaporator(content, evap_per_day, threshold):
    count = 0
    threshold = content * (threshold / 100)
    evap_per_day = evap_per_day / 100
    while content > threshold:
        content = content - content * evap_per_day
        count += 1
    return count
