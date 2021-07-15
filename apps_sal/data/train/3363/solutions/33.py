def evaporator(content, evap_per_day, threshold):
    a = 0
    threshold *=content/100
    while content >= threshold:
        a += 1
        content*=(1-evap_per_day/100)
    return a
