def evaporator(content, evap_per_day, threshold):
    d = 0
    p = content / 100 * threshold
    while content > p:
        content = content - content / 100 * evap_per_day
        d += 1
    return d
