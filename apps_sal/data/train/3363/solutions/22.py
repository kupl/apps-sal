def evaporator(content, evap_per_day, threshold):
    t = content * threshold / 100
    counter = 0
    while content >= t:
        content = content - content * evap_per_day / 100
        counter += 1
    return counter
