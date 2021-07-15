def evaporator(content, evap_per_day, threshold):
    total = 0
    threshold = content * (threshold / 100)
    evap_per_day = evap_per_day / 100
    while content > threshold:
        ev = content * evap_per_day
        content = content - ev
        total += 1
    return total
