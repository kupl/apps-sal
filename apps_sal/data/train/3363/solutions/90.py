def evaporator(content, evap_per_day, threshold):
    n = 0
    f = 100
    while f > threshold:
        f *= (1 - evap_per_day / 100)
        n += 1
    return n
