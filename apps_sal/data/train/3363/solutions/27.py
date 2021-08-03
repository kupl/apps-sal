def evaporator(content, evap, threshold):
    day = 0
    pos = content * threshold / 100
    while pos < content:
        content = content - content * (evap) / 100
        day = day + 1
    return day
