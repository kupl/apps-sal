def evaporator(content, evap_per_day, threshold):
    limit = content * threshold / 100
    evap = evap_per_day / 100
    c = 0
    while content > limit:
        content = content - content * evap
        c += 1
    return c
