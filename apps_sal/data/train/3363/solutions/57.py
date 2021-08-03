def evaporator(content, evap_per_day, threshold):
    n = 0
    ct = content * (threshold / 100)
    while (content > ct):
        content -= (content * (evap_per_day / 100))
        n += 1
    return n
