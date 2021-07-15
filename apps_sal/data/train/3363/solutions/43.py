def evaporator(content, evap_per_day, threshold):
    a = 100
    k = 0
    while a >= threshold:
        a -= a * evap_per_day / 100
        k += 1
    return k
