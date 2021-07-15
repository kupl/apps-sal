def evaporator(content, evap_per_day, threshold):
    count = 0
    og = content
    while og * threshold / 100 < content:
        content -= content * evap_per_day / 100
        count += 1
    return count
