def evaporator(content, evap_per_day, threshold):
    cday = 0
    left = content
    while left > content * (threshold / 100):
        left = left - (left * (evap_per_day / 100))
        cday += 1
    return cday
