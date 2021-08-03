def evaporator(content, evap_per_day, threshold):
    counter_days = 0
    full = 100
    while full > threshold:
        full -= full * (evap_per_day / 100)
        counter_days += 1
    return counter_days
