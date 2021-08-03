def evaporator(content, evap_per_day, threshold):

    days = 0
    current = 100.
    percent = 1 - evap_per_day / current

    while current > threshold:
        current *= percent
        days += 1

    return days
