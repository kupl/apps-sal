def evaporator(content, evap_per_day, threshold):
    c = 0
    r = 1
    while threshold/100 < r:
        r -= (evap_per_day/100 * r)
        c += 1
    return c

